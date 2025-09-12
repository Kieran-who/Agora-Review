import fs from 'fs';
import path from 'path';
import matter from 'gray-matter';
import type { DefaultTheme } from 'vitepress';

// --- Configuration ---
const contentRoot = path.resolve(__dirname, '../../content'); // Path relative to this helper file
const contentBaseUrl = '/'; // Base URL path for the root of the content
// ---------------------

/**
 * Cleans up file/directory names for display text.
 * Removes ordering prefixes, extensions, replaces separators, and title-cases.
 */
function cleanName(name: string): string {
    let cleaned = name.replace(/\.\w+$/, ''); // Remove extension
    cleaned = cleaned.replace(/^(\d+[_-]|[_-])/, ''); // Remove ordering prefixes
    cleaned = cleaned.replace(/[-_]/g, ' '); // Replace separators with space
    cleaned = cleaned.replace(/\b\w/g, char => char.toUpperCase()); // Title Case
    return cleaned.trim() || name; // Return cleaned or original if empty
}

/**
 * Generates the correct URL link for a given markdown file path and its base URL.
 * Handles index/readme files appropriately.
 * @param filePath Relative file path from the directory being scanned (e.g., 'my-doc.md', 'index.md').
 * @param baseUrl The base URL for the directory containing the file (e.g., '/guide/', '/'). Must end with '/'.
 * @returns The calculated URL string.
 */
function getFileLink(filePath: string, baseUrl: string): string {
    const fileExtension = path.extname(filePath);
    const fileNameWithoutExtension = filePath.substring(0, filePath.length - fileExtension.length);

    if (/^(index|readme)$/i.test(fileNameWithoutExtension)) {
        // Index/readme file maps to the directory's base URL
        // Ensure root index maps correctly (e.g., /index/ -> /)
        return baseUrl === `${contentBaseUrl}index/` ? contentBaseUrl : baseUrl;
    } else {
        // Other files map to base URL + filename (no extension)
        return `${baseUrl}${fileNameWithoutExtension}`;
    }
}

// --- Tag Generation ---
/**
 * Data structure for storing page info associated with a tag.
 */
interface TagPageInfo {
    link: string;
    text: string;
    relativePath: string;
}

/**
 * Scans directories recursively to find all markdown files and extracts their tags.
 * @param dirPath Absolute path to the directory to scan.
 * @param baseUrl The corresponding base URL path for this directory. Must end with '/'.
 * @param tagsMap A Map to accumulate tag data. Key: tag name, Value: array of TagPageInfo.
 * @param scanRoot The absolute path to the root content directory being scanned.
 */
function scanFilesForTags(
    dirPath: string,
    baseUrl: string,
    tagsMap: Map<string, TagPageInfo[]>,
    scanRoot: string
): void {
    if (!fs.existsSync(dirPath) || !fs.statSync(dirPath).isDirectory()) {
        return;
    }
    if (!baseUrl.endsWith('/')) {
        baseUrl += '/';
    }

    try {
        const entries = fs.readdirSync(dirPath);
        entries.forEach(entry => {
            if (entry.startsWith('.')) return; // Skip hidden

            const fullPath = path.join(dirPath, entry);
            let stats;
            try { stats = fs.statSync(fullPath); } catch { return; } // Skip if cannot stat

            if (stats.isDirectory()) {
                // Recursively scan subdirectories
                scanFilesForTags(fullPath, `${baseUrl}${entry}/`, tagsMap, scanRoot);
            } else if (stats.isFile() && entry.toLowerCase().endsWith('.md')) {
                try {
                    const fileContent = fs.readFileSync(fullPath, 'utf-8');
                    const { data: frontmatter } = matter(fileContent); // Parse frontmatter

                    // Handle tags defined as string (comma-separated) or array
                    let fileTags: string[] = [];
                    if (frontmatter.tags) {
                        if (typeof frontmatter.tags === 'string') {
                            fileTags = frontmatter.tags.split(',').map(t => t.trim()).filter(Boolean);
                        } else if (Array.isArray(frontmatter.tags)) {
                            fileTags = frontmatter.tags.map(t => String(t).trim()).filter(Boolean);
                        }
                    }

                    if (fileTags.length > 0) {
                        const link = getFileLink(entry, baseUrl);
                        // Use frontmatter title if available and non-empty, otherwise use cleaned filename
                        const text = typeof frontmatter.title === 'string' && frontmatter.title.trim()
                            ? frontmatter.title.trim()
                            : cleanName(entry);
                        // Calculate path relative to the root directory scanned for tags
                        const relativePath = path.relative(scanRoot, fullPath).replace(/\\/g, '/'); // Normalize slashes

                        fileTags.forEach(tag => {
                            const tagName = tag.trim();
                            if (!tagsMap.has(tagName)) {
                                tagsMap.set(tagName, []);
                            }
                            const tagPages = tagsMap.get(tagName)!;
                            // Avoid adding duplicates if a file is somehow processed twice
                            if (!tagPages.some(item => item.link === link)) {
                                tagPages.push({ link, text, relativePath });
                            }
                        });
                    }
                } catch (err) {
                    console.error(`[Sidebar Tags] Error processing file ${fullPath}:`, err);
                }
            }
        });
    } catch (err) {
        console.error(`[Sidebar Tags] Error reading directory ${dirPath}:`, err);
    }
}

/**
 * Generates one top-level sidebar group per tag (no "Tags" wrapper)
 * and flattens each tag's items so files appear directly under the tag.
 * The link text is set to the file's parent folder name.
 */
function generateTagsSidebarItems(scanRoot: string, baseUrl: string): DefaultTheme.SidebarItem[] {
    const tagsMap = new Map<string, TagPageInfo[]>();
    // Scan files, passing scanRoot to calculate relative paths correctly
    scanFilesForTags(scanRoot, baseUrl, tagsMap, scanRoot);

    if (tagsMap.size === 0) {
        return []; // No tags found
    }

    // Sort tags alphabetically
    const sortedTags = Array.from(tagsMap.keys()).sort((a, b) => a.localeCompare(b));

    // Build one top-level group per tag, with flattened items
    const tagGroups: DefaultTheme.SidebarItem[] = sortedTags.map(tag => {
        const pages = tagsMap.get(tag) || [];
        const items: DefaultTheme.SidebarItem[] = [];

        pages.forEach(page => {
            // parent folder = the directory containing the file
            // relativePath is normalised to use forward slashes
            const parts = page.relativePath.split('/').filter(Boolean);

            // Determine display label = parent folder name
            let label = '';
            if (parts.length >= 2) {
                const parentDir = parts[parts.length - 2];
                label = cleanName(parentDir);
            } else {
                // Fallback if the file sits at scanRoot (no parent dir)
                // Prefer given text (title/frontmatter) else filename
                label = page.text || cleanName(parts[parts.length - 1] || 'Untitled');
            }

            // Avoid duplicate links just in case
            if (!items.some(i => i.link === page.link)) {
                items.push({ text: label, link: page.link });
            }
        });

        // Sort items alphabetically by their label
        items.sort((a, b) => (a.text ?? '').localeCompare(b.text ?? ''));

        return {
            text: tag,          // each tag as a top-level group
            items,              // flattened list of pages for this tag
            collapsed: true,    // collapse by default (change to false if you prefer expanded)
        };
    });

    return tagGroups;
}



/**
 * Generates the complete VitePress sidebar configuration object.
 * Includes structure-based items and optionally a tag-based group.
 * @param scanRoot - The absolute path to the root directory containing content folders.
 * @param baseUrl - The base URL corresponding to the scanRoot.
 * @param includeTags - Whether to include the 'Tags' section. Defaults to true.
 * @returns The sidebar configuration object (`DefaultTheme.Sidebar`).
 */
export function generateSidebar(
    scanRoot: string = contentRoot,
    baseUrl: string = contentBaseUrl,
    includeTags: boolean = true
): DefaultTheme.Sidebar {
    // Only return tags as top-level groups
    const tagGroups = includeTags ? generateTagsSidebarItems(scanRoot, baseUrl) : [];
    return {
        '/': tagGroups
    };
}
