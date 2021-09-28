import Vue from 'vue'
import PageLayoutBuilder from './page-layout-builder.vue'

import { Drag, Drop } from 'vue-drag-drop';

Vue.component('drag', Drag);
Vue.component('drop', Drop);

function cb(){
  const VueVM = new Vue({
    el: '#builderApp',
    components:{
      PageLayoutBuilder
    }
  });

}

if (document.readyState != 'loading'){
  cb()
} else {
  document.addEventListener('DOMContentLoaded', cb);
}

