<template>
    <div class="myComponent">
        <h1 style="text-align: center">Vue Grid Layout</h1>
        <drag :transfer-data='1'>
          Inserisci un blocco del 8,33%
        </drag>
        <drag :transfer-data='2'>
          Inserisci un blocco del 16,66%
        </drag>
        <drag :transfer-data='3'>
          Inserisci un blocco del 25%
        </drag>
        <drag :transfer-data='4'>
          Inserisci un blocco del 33,33%
        </drag>
        <drag :transfer-data='5'>
          Inserisci un blocco del 41,66%
        </drag>
        <drag :transfer-data='6'>
          Inserisci un blocco del 50%
        </drag>
        <drag :transfer-data='7'>
          Inserisci un blocco del 58,33%
        </drag>
        <drag :transfer-data='8'>
          Inserisci un blocco del 66,66%
        </drag>
        <drag :transfer-data='9'>
          Inserisci un blocco del 75%
        </drag>
        <drag :transfer-data='10'>
          Inserisci un blocco del 83,33%
        </drag>
        <drag :transfer-data='11'>
          Inserisci un blocco del 91,66%
        </drag>
        <drag :transfer-data='12'>
          Inserisci un blocco del 100%
        </drag>

        <div class="sameOrder ok" v-if="sameOrder">ORDINE OK</div>
        <div class="sameOrder ko" v-else>ORDINE KO</div>

        <button type="button" v-if="sameOrder" @click.prevent="serialize">SERIALIZZA</button>

        <div class="rowFlex">
          <div class="large">
            <drop @drop="handleDrop">
              <grid-layout
                      ref="ld"
                      :layout.sync="layoutD"
                      :col-num="parseInt(colNum)"
                      :row-height="rowHeight"
                      :is-draggable="draggable"
                      :is-resizable="false"
                      :is-mirrored="false"
                      :prevent-collision="false"
                      :vertical-compact="false"
                      :use-css-transforms="true"
                      :responsive="false"
                      @layout-created="layoutCreatedEvent"
                      @layout-before-mount="layoutBeforeMountEvent"
                      @layout-mounted="layoutMountedEvent"
                      @layout-ready="layoutReadyEvent"
                      @layout-updated="layoutUpdatedEvent"
              >
                  <grid-item class="GridItem"  v-for="item in layoutD" :key="item.i"
                             :static="item.static"
                             :x="item.x"
                             :y="item.y"
                             :w="item.w"
                             :h="item.h"
                             :i="item.i"
                             @resize="resize"
                             @move="move"
                             @resized="resized"
                             @container-resized="containerResized"
                             @moved="moved"
                  >
                    <button type="button" @click="removeMe(item.parentReference)">Delete</button>
                    <button type="button" v-if="item.w!==12" @click="moreCols(item,'d')">+</button>
                    <button type="button" v-if="item.w!==1" @click="lessCols(item,'d')">-</button>
                  </grid-item>
              </grid-layout>
            </drop>
          </div>
          <div class="space"></div>
          <div class="small">
            <grid-layout
            ref="lt"
                    :layout.sync="layoutT"
                    :col-num="parseInt(colNum)"
                    :row-height="rowHeight"
                    :is-draggable="true"
                    :is-resizable="false"
                    :is-mirrored="false"
                    :prevent-collision="false"
                    :vertical-compact="false"
                    :use-css-transforms="true"
                    :responsive="false"
                    @layout-created="layoutCreatedEvent"
                    @layout-before-mount="layoutBeforeMountEvent"
                    @layout-mounted="layoutMountedEvent"
                    @layout-ready="layoutReadyEvent"
                    @layout-updated="layoutUpdatedEvent"
            >
                <grid-item class="GridItem"  v-for="item in layoutT" :key="item.i"
                           :static="item.static"
                           :x="item.x"
                           :y="item.y"
                           :w="item.w"
                           :h="item.h"
                           :i="item.i"
                           @resize="resize"
                           @move="move"
                           @resized="resized"
                           @container-resized="containerResized"
                           @moved="moved"
                >

                    <button type="button" v-if="item.w!==12" @click="moreCols(item,'t')">+</button>
                    <button type="button" v-if="item.w!==1" @click="lessCols(item,'t')">-</button>

                </grid-item>
            </grid-layout>
          </div>
          <div class="space"></div>
          <div class="small">
            <grid-layout
                    ref="ls"
                    :layout.sync="layoutS"
                    :col-num="parseInt(colNum)"
                    :row-height="rowHeight"
                    :is-draggable="true"
                    :is-resizable="false"
                    :is-mirrored="false"
                    :prevent-collision="false"
                    :vertical-compact="false"
                    :use-css-transforms="true"
                    :responsive="false"
                    @layout-created="layoutCreatedEvent"
                    @layout-before-mount="layoutBeforeMountEvent"
                    @layout-mounted="layoutMountedEvent"
                    @layout-ready="layoutReadyEvent"
                    @layout-updated="layoutUpdatedEvent"
            >
                <grid-item class="GridItem"  v-for="item in layoutS" :key="item.i"
                           :static="item.static"
                           :x="item.x"
                           :y="item.y"
                           :w="item.w"
                           :h="item.h"
                           :i="item.i"
                           @resize="resize"
                           @move="move"
                           @resized="resized"
                           @container-resized="containerResized"
                           @moved="moved"
                >
                    <button type="button" v-if="item.w!==12" @click="moreCols(item,'s')">+</button>
                    <button type="button" v-if="item.w!==1" @click="lessCols(item,'s')">-</button>
                </grid-item>
            </grid-layout>
          </div>
        </div>
    </div>
</template>

<script>
    import GridItem from './components/GridItem.vue';
    import GridLayout from './components/GridLayout.vue';
    // import ResponsiveGridLayout from './components/ResponsiveGridLayout.vue';
    import TestElement from './components/TestElement.vue';
    import CustomDragElement from './components/CustomDragElement.vue';
    import {getDocumentDir, setDocumentDir} from "./helpers/DOM";
    //var eventBus = require('./eventBus');
    import palette from 'google-palette'

    const blockHeightModule = 8;
    const seq = palette(['tol','qualitative','rainbow'], 40);
    //console.log(seq)

    export default {
        name: '',
        components: {
            // ResponsiveGridLayout,
            GridLayout,
            GridItem,
            TestElement,
            CustomDragElement,
        },
        data () {
          return {
            blocksHeight:blockHeightModule,
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
            serializedJson:{}
          }
        },
        mounted: function () {
          this.index = this.layoutD.length;

          this.addItem(8);
          this.addItem(4);
          this.addItem(6);
          this.addItem(6);
          this.refreshAll()


          //this.addItem(2);
          //this.addItem(2);
          //this.addItem(2);
          //this.addItem(6);
          //this.addItem(3);
          //this.addItem(5);
          //this.addItem(9);

        },
        methods: {
          setBackgrounds(){
            this.$nextTick(()=>{
              Array.from(this.$refs.ld.$el.querySelectorAll(".GridItem")).forEach((el,idx)=>el.style.backgroundColor = '#'+seq[idx]);
              Array.from(this.$refs.ls.$el.querySelectorAll(".GridItem")).forEach((el,idx)=>el.style.backgroundColor = '#'+seq[idx]);
              Array.from(this.$refs.lt.$el.querySelectorAll(".GridItem")).forEach((el,idx)=>el.style.backgroundColor = '#'+seq[idx]);

            })


            // :style="`background:${seq[item.i]}`"
            // :style="`background:${seq[item.i]}`"
            // :style="`background:${seq[item.i]}`"
          },
          adjustY(item){
            if(item.w+item.x>this.colNum){
              item.y = item.y+this.rowHeight
              item.x = 0
            }
          },
          moreCols(item,step){
            item.w++;
            this.adjustY(item);
            this.refreshAll()
          },
          lessCols(item,step){
            item.w--;
            this.refreshAll()
          },
          serialize(){

            //const grouped = this.groupBy(this.layoutD, col => col.y);

            let cont = this.addContainer();
            let row = this.addRow(cont);

            let allItems = this.sortedCopyLayout(this.layoutD).map(i=>i.parentReference);

            allItems.forEach((item,index)=>{
              if(index>3){
                //console.log(item,allItems[index-1])
              }
              this.addCol(row,{
                item,
                previous:allItems[index-1]
              })
            })

            // console.log('this.serializedJson',JSON.stringify(this.serializedJson))
            if(document.getElementById('id_form_data')){
              document.getElementById('id_form_data').value=JSON.stringify(this.serializedJson)
            }

            // this.layoutS.forEach()
            // let row = this.addRow(cont);
            // //console.log('grouped',grouped)
          },
          serializeContainer(options){
            /*
              container
              container-fluid
            */
            return {
              classes:['container'],
              rows:[]
            }
          },
          serializeRow(options){
            return {
              classes:['row'],
              cols:[]
            }
          },
          serializeCol(options){
            let classes = [];
            if(options.item){

              if(options.previous){
                Object.keys(options.item).forEach(key=>{
                  const prefix = key === 'd' ? '-lg' : key === 't' ? '-md' : '';
                  if(options.item[key].y === options.previous[key].y){
                    if(options.item[key].x > options.previous[key].x+options.previous[key].w){
                      classes = [
                      ...classes,
                      `offset${prefix}-${options.item[key].x - (options.previous[key].x+options.previous[key].w)}`
                      ]
                    }
                  }else{
                    if(options.item[key].x!==0){
                      classes = [
                        ...classes,
                        `offset${prefix}-${options.item[key].x}`
                      ]
                    }
                  }
                })
              }

              classes = [
                ...classes,
                `col-${options.item.s.w}`,
                `col-md-${options.item.t.w}`,
                `col-lg-${options.item.d.w}`
              ]
            }

            return {
              name:options.item.d.i,
              classes
            }
          },
          addCol(row,options){
            const col = this.serializeCol(options);

            if(!row.cols){
              row.cols = [col]
            }else{
              row.cols = [
                ...row.cols,
                col
              ]
            }

            return col;
          },
          addRow(container,options){
            const row = this.serializeRow(options);
            if(!container.rows){
              container.rows = [row];
            }else{
              container.rows = [
                ...container.rows,
                row
              ]
            }

            return row
          },
          addContainer(options){
            const container = this.serializeContainer(options);

            //if(!this.serializedJson.containers){
              this.serializedJson.containers = [container];
            //}else{
            //  this.serializedJson.containers = [
            //    ...this.serializedJson.containers,
            //    container
            //  ]
            //}

            return container
          },
          sortedCopyLayout(layout){
            return layout.concat().sort((a, b)=>{
                        return a.x - b.x;
                      }).sort((a, b)=>{
                        return a.y - b.y;
                      })
          },
          doAllContainersHasSameOrder(){
            //console.log('doAllContainersHasSameOrder')
            const d = this.sortedCopyLayout(this.layoutD).map(e=>e.i).join('');
            const t = this.sortedCopyLayout(this.layoutT).map(e=>e.i).join('');
            const s = this.sortedCopyLayout(this.layoutS).map(e=>e.i).join('');
            return d===t&&t===s
          },
          removeMe(item){
            this.layoutD.splice(this.layoutD.indexOf(item.d), 1);
            this.layoutT.splice(this.layoutT.indexOf(item.t), 1);
            this.layoutS.splice(this.layoutS.indexOf(item.s), 1);

            this.refreshAll()

            //this.layoutD.splice(this.layoutD.indexOf(item), 1);

          },
          refreshAll(step){
            this.roundYToModule(this.layoutD);
            this.roundYToModule(this.layoutT);
            this.roundYToModule(this.layoutS);
            this.setBackgrounds();
            this.triggerResize();
          },
          handleDrop(data,event){
            ////console.log('handleDrop',data,event);
            this.addItem(data)
          },
            clicked: function() {
                window.alert("CLICK!");
            },
            increaseWidth: function() {
                let width = document.getElementById("content").offsetWidth;
                width += 20;
                document.getElementById("content").style.width = width+"px";
            },
            decreaseWidth: function() {
                let width = document.getElementById("content").offsetWidth;
                width -= 20;
                document.getElementById("content").style.width = width+"px";
            },
            removeItem: function(item) {
                ////console.log("### REMOVE " + item.i);
                this.layout.splice(this.layout.indexOf(item), 1);
            },
            addItem: function(itemWidth) {
                // let self = this;
                ////console.log("### LENGTH: " + this.layout.length);
                ////console.log('itemWidth',itemWidth)

                const getFirstAvailableX = (rowItems) => {
                  //console.log('getFirstAvailableX')
                  return rowItems.reduce((acc,curr)=>acc+curr.w,0);
                }

                const getFirstAvailableXY = (rowIndex=0) => {
                  //console.log('getFirstAvailableXY')
                  const rowItems = this.layoutD.filter(block => block.y === rowIndex);
                  const firstAvailableX = getFirstAvailableX(rowItems);
                  if(firstAvailableX<this.colNum){
                    return {
                      x:firstAvailableX,
                      y:rowIndex
                    }
                  }else{
                    rowIndex=rowIndex+this.blocksHeight;
                    return getFirstAvailableXY(rowIndex);
                  }
                }

                const getXY = (itemWidth,rowIndex)=>{
                  //console.log('getXY')
                  let {x,y} = getFirstAvailableXY(rowIndex);

                  if( (this.colNum - x - itemWidth) >= 0){
                    return {x,y}
                  }else{
                    rowIndex=rowIndex+this.blocksHeight;
                    return getXY(itemWidth,rowIndex);
                  }
                }

                const createItem = ()=>{
                  //console.log('createItem')
                  const {x,y} = getXY(itemWidth,0);

                  // return Object.assign({}, {
                  //   "w":itemWidth,
                  //   "h":this.blocksHeight,
                  //   "x":x,//computedX,
                  //   "y":y,//computedY,
                  //   "i":this.index,
                  // })

                  let obj = Object.assign({}, {
                    d:{
                      "w":itemWidth,
                      "h":this.blocksHeight,
                      "x":x,//computedX,
                      "y":y,//computedY,
                      "i":this.index,
                    },
                    t:{
                      "w":itemWidth,
                      "h":this.blocksHeight,
                      "x":x,//computedX,
                      "y":y,//computedY,
                      "i":this.index,
                    },
                    s:{
                      "w":itemWidth,
                      "h":this.blocksHeight,
                      "x":x,//computedX,
                      "y":y,//computedY,
                      "i":this.index,
                    }
                  })
                  obj.d.parentReference = obj
                  obj.t.parentReference = obj
                  obj.s.parentReference = obj

                  return obj
                }

                let item = createItem();

                this.index++;
                this.layoutD = [...this.layoutD, item.d]
                //const itemT = JSON.parse(JSON.stringify(item))
                //const itemS = JSON.parse(JSON.stringify(item))
                //item.itemT = itemT;
                //item.itemS = itemS;
                this.layoutT = [...this.layoutT, item.t]
                this.layoutS = [...this.layoutS, item.s]
                this.setBackgrounds();
                return item;
            },
            move: function(i, newX, newY){
              //const el = this.layoutD.find(el=>el.i===i);
              //this.lastMovedBlock = el;
            },
            groupBy(list, keyGetter) {
              const map = new Map();
              list.forEach((item) => {
                 const key = keyGetter(item);
                 const collection = map.get(key);
                 if (!collection) {
                     map.set(key, [item]);
                 } else {
                     collection.push(item);
                 }
              });
              return map;
            },
            resize: function(i, newH, newW, newHPx, newWPx){

            },
            moved: function(i, newX, newY){
              //console.log("### MOVED i=" + i + ", X=" + newX + ", Y=" + newY);
              this.doAllContainersHasSameOrder();
            },
            resized: function(i, newH, newW, newHPx, newWPx){
                //console.log("### RESIZED i=" + i + ", H=" + newH + ", W=" + newW + ", H(px)=" + newHPx + ", W(px)=" + newWPx);
            },
            containerResized: function(i, newH, newW, newHPx, newWPx){
                //console.log("### CONTAINER RESIZED i=" + i + ", H=" + newH + ", W=" + newW + ", H(px)=" + newHPx + ", W(px)=" + newWPx);
            },
            triggerResize(){
              //to improve
              window.dispatchEvent(new Event('resize'));
            },
            /**
             * Add change direction button
             */
            changeDirection() {
              //console.log('changeDirection')
                let documentDirection = getDocumentDir();
                let toggle = "";
                if (documentDirection === "rtl") {
                    toggle = "ltr"
                } else {
                    toggle = "rtl"
                }
                setDocumentDir(toggle);
                //eventBus.$emit('directionchange');
            },

            layoutCreatedEvent: function(newLayout){
                //console.log("Created layout: ", newLayout)
            },
            layoutBeforeMountEvent: function(newLayout){
                //console.log("beforeMount layout: ", newLayout)
            },
            layoutMountedEvent: function(newLayout){
                //console.log("Mounted layout: ", newLayout)
            },
            layoutReadyEvent: function(newLayout){
                //console.log("Ready layout: ", newLayout)
            },
            layoutUpdatedEvent: function(newLayout){
              this.refreshAll()
            },
            getMinimumY(newLayout,newY){
              //console.log('getMinimumY')
              if(newY===0){
                return newY
              }else{
                if( newLayout.filter(item => item.y===newY-blockHeightModule).length ){
                  return newY
                }else{
                  return this.getMinimumY(newLayout,newY-blockHeightModule);
                }
              }

            },
            roundYToModule(newLayout){
              //console.log('roundYToModule')
              newLayout.forEach((el)=>{
                //const el = this.lastMovedBlock;
                let newY=0;
                if(el.y%blockHeightModule===0){
                  newY = el.y
                }else if(el.y%blockHeightModule>2){
                  newY = blockHeightModule*(Math.ceil(el.y/blockHeightModule));
                }else{
                  newY = blockHeightModule*(Math.floor(el.y/blockHeightModule));
                }
                el.y = this.getMinimumY(newLayout,newY);
              })
            }

        },
        computed:{
          sameOrder(){
            return this.doAllContainersHasSameOrder()
          }
        }
    }
</script>

<style>
    /*    #app {
            font-family: 'Avenir', Helvetica, Arial, sans-serif;
            -webkit-font-smoothing: antialiased;
            -moz-osx-font-smoothing: grayscale;
            text-align: center;
            color: #2c3e50;
            margin-top: 60px;
        }

        h1, h2 {
            font-weight: normal;
        }

        ul {
            list-style-type: none;
            padding: 0;
        }

        li {
            display: inline-block;
            margin: 0 10px;
        }

        a {
            color: #42b983;
        }*/
</style>

<style lang="scss">
.popup #content {
  margin:0;
  padding:20px;
  box-sizing: border-box;
}
  .myComponent {
    width:100%;
    display:block;
    font-family: 'Avenir', Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    /*text-align: center;*/
    color: #2c3e50;
    /*margin-top: 60px;*/
  }
  .sameOrder{
    padding:20px 0;
    font-size:18px;
    font-weight:bold;
    &.ok{
      color:green;
    }
    &.ko{
      color:red;
    }
  }
  .rowFlex{
    display:flex;
    flex-flow: row nowrap;
  }
  .large{
    flex:0 0 40%;
  }
  .space{
    flex:0 0 2%;
  }
  .small{
    flex:0 0 28%;
  }
</style>
