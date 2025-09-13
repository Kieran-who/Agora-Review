import MyLayout from './MyLayout.vue';
import DefaultTheme from 'vitepress/theme';
import PreviousDiscussions from './PreviousDiscussions.vue';
import './custom.css';

export default {
  extends: DefaultTheme,
  Layout: MyLayout,
  enhanceApp({ app }) {
    // Register custom components
    app.component('PreviousDiscussions', PreviousDiscussions);
  },
};
