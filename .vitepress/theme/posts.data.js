import { createContentLoader } from 'vitepress';

export default createContentLoader('*/*.md', {
  transform: (content) => {
    return content.filter(
      (post) => !post.frontmatter.title.includes('Transcript')
    );
  },
});
