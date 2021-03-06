import Vue from 'vue';
import PageLayoutBuilder from './components/page-layout-builder.vue';
import 'bootstrap/dist/css/bootstrap.min.css';

import { Drag, Drop } from 'vue-drag-drop';

Vue.component('Drag', Drag);
Vue.component('Drop', Drop);

const VueVM = new Vue({
  el: '#app',
  components: {
    PageLayoutBuilder,
  },
  template: `<page-layout-builder
    :i18n='{
      componentTitle:"Page Layout Builder",
      componentDescription:"<p>Using this interface you will be able to create the layout of a new page. You will define before containers and after columns that will be the wrapper for your widgets plugins</p><p>First of all create your containers from the button &apos;Add container&apos;. There are two types of containers, boxed and fluid. The fluid one will be full width, while the boxed one will be centered with the max width defined from the grid system. They will be showed in the layout preview sections with a gray background and a blue border.</p><p>Now you can place, with drag & drop the colums. The columns can have a size from 1 to 12 (8,33% to 100%). Drag the desired column from the panel below the layouts inside a container in the Desktop layout. Be careful! Tablet and Smartphone layout will be automatically updated, you can&apos;t drag columns in them</p>",
      buttonsTitle:"AVAILABLE CONTAINERS",
      addBoxedContainer:"ADD CONTAINER BOXED",
      addFluidContainer:"ADD CONTAINER FLUID",
      layoutTitleD:"DESKTOP",
      layoutTitleT:"TABLET",
      layoutTitleS:"SMARTPHONE",
      pageHeader:"PAGE HEADER",
      pageFooter:"PAGE FOOTER",
      del:"Delete",
      colsTitle:"AVAILABLE COLUMNS",
      errorCols:"Check the order of the columns! It should be the same for each responsive step!",
      errorContainers:"Add at least one container and one col to proceed",
      colBigPrefix:"COL",
      colSmallPrefix:"C"
    }'
  ></page-layout-builder>`,
});
