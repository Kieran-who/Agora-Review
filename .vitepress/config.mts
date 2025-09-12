import { withMermaid } from "vitepress-plugin-mermaid"
import { generateSidebar } from './helpers/sidebar';


// https://vitepress.dev/reference/site-config
export default withMermaid({
  title: "The Agora Review",

  description: "This is a great place to write a something about your project.",
  srcDir: './content',

  head: [
    ['link', { rel: 'icon', type: 'image/png', href: '/favicon-96x96.png', sizes: '96x96' }],
    ['link', { rel: 'icon', type: 'image/svg+xml', href: '/favicon.svg' }],
    ['link', { rel: 'apple-touch-icon', sizes: "180x180", href: "/apple-touch-icon.png" }],
    ['link', { rel: 'shortcut icon', href: '/favicon.ico' }],
    ['link', { rel: 'manifest', href: '/site.webmanifest' }],
    ['meta', { name: "theme-color", content: 'default' }],
    ['meta', { name: 'apple-mobile-web-app-title', content: 'Agora Review' }],
    ['meta', { name: 'application-name', content: 'The Agora Review' }],
    ['meta', { name: 'viewport', content: 'width=device-width, initial-scale=1.0' }],
  ],

  themeConfig: {
    logo: '/hero.png',
    nav: [
      { text: 'Home', link: '/' },
      { text: 'Info', link: '/info' },
    ],

    search: {
      provider: 'local'
    },
    sidebar: generateSidebar(),

    socialLinks: [
      { icon: 'github', link: 'https://github.com/Kieran-who/Agora-Review' }
    ],
    footer: {
      message: 'AI-generated content. Always review for accuracy.',
      copyright: 'Copyright © 2025-present Kieran'
    }
  },
  cleanUrls: true,
  markdown: {
    math: true,
    image: {
      lazyLoading: true
    }
  },
  mermaid: {}
})
