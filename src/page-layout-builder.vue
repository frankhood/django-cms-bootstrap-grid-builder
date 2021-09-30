<template>
  <div id="plbSpecificity" class="pageLayoutBuilder">
    <h2 class="componentTitle">{{ i18n.componentTitle }}</h2>
    <div class="componentDescription" v-html="i18n.componentDescription" />
    <div class="containersBtns">
      <h3 class="buttonsTitle">{{ i18n.buttonsTitle }}</h3>
      <button type="button" @click.prevent="addBoxedContainer">
        {{ i18n.addBoxedContainer }}
      </button>
      <button type="button" @click.prevent="addFluidContainer">
        {{ i18n.addFluidContainer }}
      </button>
    </div>
    <div class="rowFlex layoutsWrapper">
      <div class="large">
        <h3 class="layoutTitle">{{ i18n.layoutTitleD }}</h3>
        <div class="page">
          <header class="pageHeader">{{ i18n.pageHeader }}</header>
          <template v-for="(container, i) in containers">
            <drop
              :key="'LargeDropzone' + i"
              class="dropzone"
              @drop="
                (data, event) => {
                  handleDrop(data, event, container);
                }
              "
            >
              <button
                :class="['deleteContainer', { deleteBoxed: container.boxed }]"
                type="button"
                @click="removeContainer(container)"
              >
                {{ i18n.del }}
              </button>
              <grid-layout
                :class="['containerPrototype', { boxed: container.boxed }]"
                :layout.sync="container.layoutD"
                :col-num="parseInt(colNum)"
                :row-height="rowHeight"
                :is-draggable="draggable"
                :is-resizable="false"
                :is-mirrored="false"
                :prevent-collision="false"
                :vertical-compact="false"
                :use-css-transforms="true"
                :responsive="false"
                @layout-updated="layoutUpdatedEvent"
              >
                <grid-item
                  v-for="item in container.layoutD"
                  :key="item.i"
                  class="GridItem"
                  :style="computedItemStyle(item.i)"
                  :static="item.static"
                  :x="item.x"
                  :y="item.y"
                  :w="item.w"
                  :h="item.h"
                  :i="item.i"
                  @resize="resize"
                  @moved="moved"
                >
                  <button
                    type="button"
                    class="utilityCta"
                    @click="removeMe(item)"
                  >
                    <svg
                      id="Capa_1"
                      version="1.1"
                      xmlns="http://www.w3.org/2000/svg"
                      xmlns:xlink="http://www.w3.org/1999/xlink"
                      x="0px"
                      y="0px"
                      viewBox="0 0 388.245 388.245"
                      style="enable-background: new 0 0 388.245 388.245"
                      xml:space="preserve"
                    >
                      <g>
                        <path
                          style="fill: #010002"
                          d="M107.415,388.245h173.334c21.207,0,38.342-17.159,38.342-38.342V80.928H69.097v268.975
                            C69.097,371.086,86.264,388.245,107.415,388.245z M253.998,129.643c0-7.178,5.796-13.03,13.006-13.03
                            c7.178,0,13.006,5.853,13.006,13.03v208.311c0,7.21-5.828,13.038-13.006,13.038c-7.21,0-13.006-5.828-13.006-13.038V129.643z
                             M181.491,129.643c0-7.178,5.804-13.03,13.006-13.03c7.178,0,13.006,5.853,13.006,13.03v208.311c0,7.21-5.828,13.038-13.006,13.038
                            c-7.202,0-13.006-5.828-13.006-13.038C181.491,337.954,181.491,129.643,181.491,129.643z M109.025,129.643
                            c0-7.178,5.796-13.03,12.973-13.03s13.038,5.853,13.038,13.03v208.311c0,7.21-5.861,13.038-13.038,13.038
                            c-7.178,0-12.973-5.828-12.973-13.038V129.643z"
                        />
                        <path
                          style="fill: #010002"
                          d="M294.437,20.451h-52.779C240.39,8.966,230.75,0,218.955,0h-49.682
                            c-11.86,0-21.476,8.966-22.736,20.451H93.792c-25.865,0-46.756,20.955-46.902,46.756h294.466
                            C341.258,41.407,320.335,20.451,294.437,20.451z"
                        />
                      </g>
                    </svg>
                  </button>
                  <button
                    v-if="item.w !== 12"
                    type="button"
                    class="utilityCta"
                    @click="moreCols(item, 'd')"
                  >
                    +
                  </button>
                  <button
                    v-if="item.w !== 1"
                    type="button"
                    class="utilityCta"
                    @click="lessCols(item, 'd')"
                  >
                    -
                  </button>
                </grid-item>
              </grid-layout>
            </drop>
          </template>
          <footer class="pageFooter">{{ i18n.pageFooter }}</footer>
        </div>
      </div>
      <div class="space"></div>
      <div class="medium">
        <h3 class="layoutTitle">{{ i18n.layoutTitleT }}</h3>
        <div class="page">
          <header class="pageHeader">{{ i18n.pageHeader }}</header>
          <template v-for="(container, i) in containers">
            <div :key="'MediumDropzone' + i" class="dropzone fakeDropzone">
              <grid-layout
                :class="['containerPrototype', { boxed: container.boxed }]"
                :layout.sync="container.layoutT"
                :col-num="parseInt(colNum)"
                :row-height="rowHeight"
                :is-draggable="true"
                :is-resizable="false"
                :is-mirrored="false"
                :prevent-collision="false"
                :vertical-compact="false"
                :use-css-transforms="true"
                :responsive="false"
                @layout-updated="layoutUpdatedEvent"
              >
                <grid-item
                  v-for="item in container.layoutT"
                  :key="item.i"
                  class="GridItem"
                  :style="computedItemStyle(item.i)"
                  :static="item.static"
                  :x="item.x"
                  :y="item.y"
                  :w="item.w"
                  :h="item.h"
                  :i="item.i"
                  @resize="resize"
                  @moved="moved"
                >
                  <button
                    v-if="item.w !== 12"
                    type="button"
                    class="utilityCta"
                    @click="moreCols(item, 't')"
                  >
                    +
                  </button>
                  <button
                    v-if="item.w !== 1"
                    type="button"
                    class="utilityCta"
                    @click="lessCols(item, 't')"
                  >
                    -
                  </button>
                </grid-item>
              </grid-layout>
            </div>
          </template>
          <footer class="pageFooter">{{ i18n.pageFooter }}</footer>
        </div>
      </div>
      <div class="space"></div>
      <div class="small">
        <h3 class="layoutTitle">{{ i18n.layoutTitleS }}</h3>
        <div class="page">
          <header class="pageHeader">{{ i18n.pageHeader }}</header>
          <template v-for="(container, i) in containers">
            <div :key="'SmallDropzone' + i" class="dropzone fakeDropzone">
              <grid-layout
                :class="['containerPrototype', { boxed: container.boxed }]"
                :layout.sync="container.layoutS"
                :col-num="parseInt(colNum)"
                :row-height="rowHeight"
                :is-draggable="true"
                :is-resizable="false"
                :is-mirrored="false"
                :prevent-collision="false"
                :vertical-compact="false"
                :use-css-transforms="true"
                :responsive="false"
                @layout-updated="layoutUpdatedEvent"
              >
                <grid-item
                  v-for="item in container.layoutS"
                  :key="item.i"
                  class="GridItem"
                  :style="computedItemStyle(item.i)"
                  :static="item.static"
                  :x="item.x"
                  :y="item.y"
                  :w="item.w"
                  :h="item.h"
                  :i="item.i"
                  @resize="resize"
                  @moved="moved"
                >
                  <button
                    v-if="item.w !== 12"
                    type="button"
                    class="utilityCta"
                    @click="moreCols(item, 's')"
                  >
                    +
                  </button>
                  <button
                    v-if="item.w !== 1"
                    type="button"
                    class="utilityCta"
                    @click="lessCols(item, 's')"
                  >
                    -
                  </button>
                </grid-item>
              </grid-layout>
            </div>
          </template>
          <footer class="pageFooter">{{ i18n.pageFooter }}</footer>
        </div>
      </div>
    </div>
    <div class="rowFlex">
      <div class="exampleContainer">
        <h3 class="colsTitle">{{ i18n.colsTitle }}</h3>
        <drag class="col col-1" :transfer-data="1">
          <div class="brick">{{ i18n.colSmallPrefix }} 1</div>
        </drag>
        <drag class="col col-11" :transfer-data="11">
          <div class="brick">{{ i18n.colBigPrefix }} 11</div>
        </drag>
        <drag class="col col-2" :transfer-data="2">
          <div class="brick">{{ i18n.colBigPrefix }} 2</div>
        </drag>
        <drag class="col col-10" :transfer-data="10">
          <div class="brick">{{ i18n.colBigPrefix }} 10</div>
        </drag>
        <drag class="col col-3" :transfer-data="3">
          <div class="brick">{{ i18n.colBigPrefix }} 3</div>
        </drag>
        <drag class="col col-9" :transfer-data="9">
          <div class="brick">{{ i18n.colBigPrefix }} 9</div>
        </drag>
        <drag class="col col-4" :transfer-data="4">
          <div class="brick">{{ i18n.colBigPrefix }} 4</div>
        </drag>
        <drag class="col col-8" :transfer-data="8">
          <div class="brick">{{ i18n.colBigPrefix }} 8</div>
        </drag>
        <drag class="col col-5" :transfer-data="5">
          <div class="brick">{{ i18n.colBigPrefix }} 5</div>
        </drag>
        <drag class="col col-7" :transfer-data="7">
          <div class="brick">{{ i18n.colBigPrefix }} 7</div>
        </drag>
        <drag class="col col-6" :transfer-data="6">
          <div class="brick">{{ i18n.colBigPrefix }} 6</div>
        </drag>
        <drag class="col col-6" :transfer-data="6">
          <div class="brick">{{ i18n.colBigPrefix }} 6</div>
        </drag>
        <drag class="col col-12" :transfer-data="12">
          <div class="brick">{{ i18n.colBigPrefix }} 12</div>
        </drag>
      </div>
    </div>
    <div class="actionsWrapper">
      <div v-if="!sameOrder" class="sameOrder ko">{{ i18n.errorCols }}</div>
      <div v-else-if="!hasCols" class="sameOrder ko">
        {{ i18n.errorContainers }}
      </div>
      <button v-else type="button" class="saveBtn" @click.prevent="serialize">
        SALVA
      </button>
    </div>
  </div>
</template>

<script>
import GridItem from './components/GridItem.vue';
import GridLayout from './components/GridLayout.vue';
import { getDocumentDir, setDocumentDir } from './helpers/DOM';
import palette from 'google-palette';

const blockHeightModule = 8;
const seq = palette(['tol', 'qualitative', 'rainbow'], 40);

export default {
  name: 'PageLayoutBuilder',
  components: {
    GridLayout,
    GridItem,
  },
  props: ['i18n'],
  data() {
    return {
      allItems: [],
      containers: [],
      blocksHeight: blockHeightModule,
      layoutD: [],
      layoutT: [],
      layoutS: [],
      draggable: true,
      resizable: true,
      mirrored: false,
      responsive: true,
      preventCollision: false,
      rowHeight: blockHeightModule,
      colNum: 12,
      index: 0,
      indexContainer: 0,
      serializedJson: {},
    };
  },
  computed: {
    sameOrder() {
      return this.doAllContainersHasSameOrder();
    },
    hasCols() {
      return this.containers.length && this.containers[0].layoutD.length;
    },
  },
  mounted: function () {
    if (
      document.getElementById('json-data') &&
      document.getElementById('json-data').value.length
    ) {
      const data = JSON.parse(document.getElementById('json-data').value);
      this.containers = data;
    }
    if (window.CMS) {
      window.CMS.$('form')
        .off('submit.myWidgetNs')
        .on('submit.myWidgetNs', (e) => {
          if (
            !e.originalEvent.submitter.getAttribute('name') ||
            e.originalEvent.submitter.getAttribute('name') !==
              'wizard_goto_step'
          ) {
            let savedHeight;
            if (!this.sameOrder) {
              e.preventDefault();
              savedHeight = window.pageYOffset;
              alert(this.i18n.errorCols);
              if (window.parent && window.parent.CMS) {
                setTimeout(() => {
                  window.parent.CMS.$('.cms-modal-frame iframe').css(
                    'display',
                    'block'
                  );
                  window.scrollTo(0, savedHeight);
                }, 100);
              }
            } else if (!this.hasCols) {
              e.preventDefault();
              savedHeight = window.pageYOffset;
              alert(this.i18n.errorContainers);
              if (window.parent && window.parent.CMS) {
                setTimeout(() => {
                  window.parent.CMS.$('.cms-modal-frame iframe').css(
                    'display',
                    'block'
                  );
                  window.scrollTo(0, savedHeight);
                }, 100);
              }
            } else {
              this.serialize();
            }
          }
        });
    }
  },
  methods: {
    computedItemStyle(idx) {
      return {
        backgroundColor: '#' + seq[idx],
      };
    },
    addBoxedContainer() {
      this.containers = [
        ...this.containers,
        {
          indexContainer: this.indexContainer,
          boxed: true,
          layoutD: [],
          layoutT: [],
          layoutS: [],
        },
      ];
      this.indexContainer++;
    },
    addFluidContainer() {
      this.containers = [
        ...this.containers,
        {
          indexContainer: this.indexContainer,
          boxed: false,
          layoutD: [],
          layoutT: [],
          layoutS: [],
        },
      ];
      this.indexContainer++;
    },
    adjustY(item) {
      if (item.w + item.x > this.colNum) {
        item.y = item.y + this.rowHeight;
        item.x = 0;
      }
    },
    moreCols(item, step) {
      item.w++;
      this.adjustY(item);
      this.refreshAll();
    },
    lessCols(item, step) {
      item.w--;
      this.refreshAll();
    },
    serialize() {
      this.containers.forEach((container) => {
        let cont = this.addContainer(container);
        let row = this.addRow(cont);

        let allItemsD = this.sortedCopyLayout(container.layoutD);
        let allItemsT = this.sortedCopyLayout(container.layoutT);
        let allItemsS = this.sortedCopyLayout(container.layoutS);

        let allItems = allItemsD.map((d, idx) => {
          return {
            d: d,
            t: allItemsT[idx],
            s: allItemsS[idx],
            index: d.i,
          };
        });

        allItems.forEach((item, index) => {
          this.addCol(row, {
            item,
            previous: allItems[index - 1],
          });
        });
      });

      try {
        if (document.querySelector('form .form-row.form_data textarea')) {
          document.querySelector('form .form-row.form_data textarea').value =
            JSON.stringify(this.serializedJson);
        }
        if (document.querySelector('form .form-row.field-form_data textarea')) {
          document.querySelector(
            'form .form-row.field-form_data textarea'
          ).value = JSON.stringify(this.serializedJson);
        }
        if (document.getElementById('json-data')) {
          document.getElementById('json-data').value = JSON.stringify(
            this.containers
          );
        }
      } catch (e) {
        // eslint-disable-next-line
        console.error(e);
      }
    },
    serializeContainer(options) {
      if (options.boxed) {
        return {
          attrs: { variant_class: 'container' },
          rows: [],
        };
      } else {
        return {
          attrs: { variant_class: 'container-fluid' },
          rows: [],
        };
      }
    },
    serializeRow(options) {
      return {
        attrs: { variant_class: '' },
        cols: [],
      };
    },
    serializeCol(options) {
      let classes = {};
      if (options.item) {
        if (options.previous) {
          Object.keys(options.item).forEach((key) => {
            const prefix = key === 'd' ? '-lg' : key === 't' ? '-md' : '';
            if (options.item[key].y === options.previous[key].y) {
              if (
                options.item[key].x >
                options.previous[key].x + options.previous[key].w
              ) {
                classes = {
                  ...classes,
                  [`offset_${prefix}`]:
                    options.item[key].x -
                    (options.previous[key].x + options.previous[key].w),
                };
              }
            } else {
              if (options.item[key].x !== 0) {
                classes = {
                  ...classes,
                  [`offset_${prefix}`]: options.item[key].x,
                };
              }
            }
          });
        }

        classes = {
          ...classes,
          cols_xs: options.item.s.w,
          cols_md: options.item.t.w,
          cols_lg: options.item.d.w,
        };
      }

      return {
        name: options.item.d.i,
        attrs: classes,
      };
    },
    addCol(row, options) {
      const col = this.serializeCol(options);

      if (!row.cols) {
        row.cols = [col];
      } else {
        row.cols = [...row.cols, col];
      }

      return col;
    },
    addRow(container, options) {
      const row = this.serializeRow(options);

      if (!container.rows) {
        container.rows = [row];
      } else {
        container.rows = [...container.rows, row];
      }

      return row;
    },
    addContainer(options) {
      const container = this.serializeContainer(options);

      if (!this.serializedJson.containers) {
        this.serializedJson.containers = [container];
      } else {
        this.serializedJson.containers = [
          ...this.serializedJson.containers,
          container,
        ];
      }

      return container;
    },
    sortedCopyLayout(layout) {
      return layout
        .concat()
        .sort((a, b) => {
          return a.x - b.x;
        })
        .sort((a, b) => {
          return a.y - b.y;
        });
    },
    doAllContainersHasSameOrder() {
      return this.containers.reduce((acc, curr) => {
        const d = this.sortedCopyLayout(curr.layoutD)
          .map((e) => e.i)
          .join('');
        const t = this.sortedCopyLayout(curr.layoutT)
          .map((e) => e.i)
          .join('');
        const s = this.sortedCopyLayout(curr.layoutS)
          .map((e) => e.i)
          .join('');
        return acc && d === t && t === s;
      }, true);
    },
    removeContainer(container) {
      this.containers.splice(this.containers.indexOf(container), 1);
    },
    removeMe(item) {
      let container = this.containers.find(
        (o) => o.indexContainer === item.indexContainer
      );
      const elementToDeleteD = container.layoutD.find((o) => o.i === item.i);
      const elementToDeleteT = container.layoutT.find((o) => o.i === item.i);
      const elementToDeleteS = container.layoutS.find((o) => o.i === item.i);
      container.layoutD.splice(container.layoutD.indexOf(elementToDeleteD), 1);
      container.layoutT.splice(container.layoutT.indexOf(elementToDeleteT), 1);
      container.layoutS.splice(container.layoutS.indexOf(elementToDeleteS), 1);
      this.refreshAll();
    },
    refreshAll(step) {
      this.containers.forEach((container) => {
        this.roundYToModule(container.layoutD);
        this.roundYToModule(container.layoutT);
        this.roundYToModule(container.layoutS);
      });
      this.triggerResize();
    },
    handleDrop(data, event, container) {
      this.addItem(data, container);
    },
    addItem: function (itemWidth, container) {
      const getFirstAvailableX = (rowItems) => {
        return rowItems.reduce((acc, curr) => acc + curr.w, 0);
      };

      const getFirstAvailableXY = (rowIndex = 0) => {
        const rowItems = container.layoutD.filter(
          (block) => block.y === rowIndex
        );
        const firstAvailableX = getFirstAvailableX(rowItems);
        if (firstAvailableX < this.colNum) {
          return {
            x: firstAvailableX,
            y: rowIndex,
          };
        } else {
          rowIndex = rowIndex + this.blocksHeight;
          return getFirstAvailableXY(rowIndex);
        }
      };

      const getXY = (itemWidth, rowIndex) => {
        let { x, y } = getFirstAvailableXY(rowIndex);

        if (this.colNum - x - itemWidth >= 0) {
          return { x, y };
        } else {
          rowIndex = rowIndex + this.blocksHeight;
          return getXY(itemWidth, rowIndex);
        }
      };

      const createItem = () => {
        const { x, y } = getXY(itemWidth, 0);
        let obj = Object.assign(
          {},
          {
            d: {
              w: itemWidth,
              h: this.blocksHeight,
              x: x,
              y: y,
              i: this.index,
              indexContainer: container.indexContainer,
            },
            t: {
              w: itemWidth,
              h: this.blocksHeight,
              x: x,
              y: y,
              i: this.index,
              indexContainer: container.indexContainer,
            },
            s: {
              w: itemWidth,
              h: this.blocksHeight,
              x: x,
              y: y,
              i: this.index,
              indexContainer: container.indexContainer,
            },
          }
        );
        obj.index = this.index;
        return obj;
      };

      let item = createItem();

      this.index++;
      container.layoutD = [...container.layoutD, item.d];
      container.layoutT = [...container.layoutT, item.t];
      container.layoutS = [...container.layoutS, item.s];
      return item;
    },
    resize: function (i, newH, newW, newHPx, newWPx) {},
    moved: function (i, newX, newY) {
      this.doAllContainersHasSameOrder();
    },
    triggerResize() {
      window.dispatchEvent(new Event('resize'));
    },
    layoutUpdatedEvent: function (newLayout) {
      this.refreshAll();
    },
    getMinimumY(newLayout, newY) {
      if (newY === 0) {
        return newY;
      } else {
        if (
          newLayout.filter((item) => item.y === newY - blockHeightModule).length
        ) {
          return newY;
        } else {
          return this.getMinimumY(newLayout, newY - blockHeightModule);
        }
      }
    },
    roundYToModule(newLayout) {
      newLayout.forEach((el) => {
        let newY = 0;
        if (el.y % blockHeightModule === 0) {
          newY = el.y;
        } else if (el.y % blockHeightModule > 2) {
          newY = blockHeightModule * Math.ceil(el.y / blockHeightModule);
        } else {
          newY = blockHeightModule * Math.floor(el.y / blockHeightModule);
        }
        el.y = this.getMinimumY(newLayout, newY);
      });
    },
  },
};
</script>

<style lang="scss">
#plbSpecificity {
  button {
    outline: 0;
    user-select: none;
    border: 0;
  }

  &.pageLayoutBuilder {
    width: 100%;
    display: block;
    color: #2c3e50;
    clear: both;
  }

  .utilityCta {
    appearance: none;
    border: none;
    padding: 5px;
    font-size: 18px;
    line-height: 12px;
    vertical-align: top;
    background: #417690;
    color: #fff;
    min-width: 26px;
    min-height: 26px;
    user-select: none;
    transition: all 0.4s ease;
    cursor: pointer;

    svg {
      user-select: none;
      width: 15px;
      height: 15px;
      fill: #fff !important;
      stroke: #fff !important;

      * {
        fill: #fff !important;
        stroke: #fff !important;
      }
    }

    &:hover {
      user-select: none;

      background: #205067;
    }

    &:focus {
      outline: 0 !important;
      border: 0 !important;
    }

    &:active {
      background: #417690;
    }
  }

  .componentTitle {
    font-size: 32px;
    color: #000;
    line-height: 1.3;
    margin: 0 0 20px;
    font-weight: 600;
    padding: 0;
    background: transparent;
  }

  .componentDescription {
    font-size: 18px;
    p {
      padding-bottom: 10px;
    }
  }

  .containersBtns {
    display: flex;
    flex-flow: row wrap;
    justify-content: flex-start;
    margin: 30px 0 0;

    button {
      background: #417690;
      appearance: none;
      text-transform: uppercase;
      font-weight: 400;
      padding: 10px 15px;
      margin: 0 10px 0 0;
      border-radius: 0;
      color: #fff;
      cursor: pointer;
      height: 45px;
      line-height: 20px;
      font-size: 18px;

      &:hover,
      &:focus {
        background: #205067;
      }
    }
  }

  .layoutTitle,
  .buttonsTitle,
  .colsTitle {
    text-align: left;
    background: none;
    color: black;
    font-size: 22px;
    margin: 0 0 20px;
    line-height: 40px;
    font-weight: 600;
    padding: 0;
  }

  .buttonsTitle {
    width: 100%;
  }

  .colsTitle {
    width: 100%;
  }

  .layoutsWrapper {
    margin: 30px 0 0;
  }

  .page {
    border: 2px solid black;
    min-height: 127px;
    position: relative;
    padding: 40px 0 41px;
  }

  .large {
    flex: 0 0 48%;
  }

  .medium {
    flex: 0 0 28%;
  }

  .small {
    flex: 0 0 20%;
  }

  .pageHeader {
    text-align: center;
    font-weight: 700;
    font-size: 16px;
    width: 100%;
    height: 40px;
    top: 0;
    position: absolute;
    line-height: 40px;
    background-color: #dadada;
  }

  .pageFooter {
    text-align: center;
    font-weight: 700;
    font-size: 16px;
    width: 100%;
    height: 40px;
    bottom: 0;
    position: absolute;
    line-height: 40px;
    background-color: #dadada;
  }

  .actionsWrapper {
    margin: 40px 0 0;
    text-align: right;
  }

  .exampleContainer {
    margin: 30px 0 0;
    display: flex;
    flex-flow: row wrap;
    width: 48%;

    .col {
      padding: 2px;
      overflow: hidden;

      .brick {
        background: #417690;
        appearance: none;
        text-transform: uppercase;
        font-weight: 400;
        padding: 13px 6px;
        margin: 5px 5px 5px 0;
        border-radius: 0;
        color: #fff;
        cursor: pointer;
        height: 45px;
        line-height: 18px;
        font-size: 18px;
        text-align: center;

        &:hover,
        &:focus {
          background: #205067;
        }
      }
    }

    .col-1 {
      flex-basis: 8.33%;
      flex-grow: 0;
      flex-shrink: 0;
    }

    .col-2 {
      flex-basis: 16.66%;
      flex-grow: 0;
      flex-shrink: 0;
    }

    .col-3 {
      flex-basis: 25%;
      flex-grow: 0;
      flex-shrink: 0;
    }

    .col-4 {
      flex-basis: 33.33%;
      flex-grow: 0;
      flex-shrink: 0;
    }

    .col-5 {
      flex-basis: 41.66%;
      flex-grow: 0;
      flex-shrink: 0;
    }

    .col-6 {
      flex-basis: 50%;
      flex-grow: 0;
      flex-shrink: 0;
    }

    .col-7 {
      flex-basis: 58.33%;
      flex-grow: 0;
      flex-shrink: 0;
    }

    .col-8 {
      flex-basis: 66.66%;
      flex-grow: 0;
      flex-shrink: 0;
    }

    .col-9 {
      flex-basis: 75%;
      flex-grow: 0;
      flex-shrink: 0;
    }

    .col-10 {
      flex-basis: 83.33%;
      flex-grow: 0;
      flex-shrink: 0;
    }

    .col-11 {
      flex-basis: 91.66%;
      flex-grow: 0;
      flex-shrink: 0;
    }

    .col-12 {
      flex-basis: 100%;
      flex-grow: 0;
      flex-shrink: 0;
    }
  }

  .dropzone {
    padding: 1px 0;
    position: relative;
  }

  .deleteContainer {
    position: absolute;
    top: 5px;
    right: 5px;
    z-index: 99999;
    background: #417690;
    color: #fff;
    appearance: none;
    border: 0;
    margin: 0;
    padding: 3px 10px;
    line-height: 15px;
    font-size: 15px;
    user-select: none;
    transition: all 0.4s ease;
    cursor: pointer;

    &:hover {
      user-select: none;
      background: #205067;
    }

    &:focus {
      outline: 0 !important;
      border: 0 !important;
    }

    &:active {
      background: #417690;
    }

    &.deleteBoxed {
      margin-right: 10%;
    }
  }

  .boxed {
    margin: 0 10%;
  }

  .containerPrototype {
    min-height: 40px;
    outline: 2px #417690 solid;
    box-sizing: border-box;
  }

  .popup #content {
    margin: 0;
    padding: 20px;
    box-sizing: border-box;
  }

  .sameOrder {
    padding: 20px 0;
    font-size: 18px;
    font-weight: bold;

    &.ok {
      color: green;
    }

    &.ko {
      color: red;
    }
  }

  .rowFlex {
    display: flex;
    flex-flow: row nowrap;
  }

  .space {
    flex: 0 0 2%;
  }
}
</style>
