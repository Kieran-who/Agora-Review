import MyLayout from './MyLayout.vue';
import DefaultTheme from 'vitepress/theme';
import './custom.css';

export default {
  extends: DefaultTheme,
  Layout: MyLayout,
};
