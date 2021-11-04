import Vue from 'vue';
import PageLayoutBuilder from './components/page-layout-builder.vue';

import { Drag, Drop } from 'vue-drag-drop';

Vue.component('Drag', Drag);
Vue.component('Drop', Drop);

function cb() {
  const VueVM = new Vue({
    el: '#builderApp',
    components: {
      PageLayoutBuilder,
    },
  });
}

if (document.readyState != 'loading') {
  cb();
} else {
  document.addEventListener('DOMContentLoaded', cb);
}
