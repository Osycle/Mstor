<template>
  <div class="index-wrapper">
    <div class="container-fluid">
      <nuxt-link to="/test">Тест</nuxt-link>
      <Modal v-if="modal_open_status" :modal-data="cells" @modal-manager="modalManager"/>
      <div class="cells">
        {{cells.length}}
        <div class="cell" v-for="(cell, key) in cells" :key="key">
          <div class="cell-wrapper">
            <div class="date-content">
              {{ new Date(cell.date_time) | dateFormat('D MMMM YYYY')}}
            </div>
            <div class="img-content"></div>
            <div class="text-content">
              <span class="cell-title">{{cell.title}}</span>
              <span v-html="cell.description"></span>
            </div>
            <div class="btn-content">
              <button type="button" class="btn-edit" title="Редактировать">
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 101 101"><path d="M82.2 79.2H18.8c-1.3 0-2.4 1.1-2.4 2.4s1.1 2.4 2.4 2.4h63.4c1.3 0 2.4-1.1 2.4-2.4s-1.1-2.4-2.4-2.4zM16.5 58.2l-.1 11.3c0 .6.2 1.3.7 1.7.5.4 1.1.7 1.7.7l11.3-.1c.6 0 1.2-.3 1.7-.7l38.8-38.8c.9-.9.9-2.5 0-3.4L59.4 17.7c-.9-.9-2.5-.9-3.4 0l-7.8 7.8-31 31c-.5.5-.7 1.1-.7 1.7zm49-27.6L61.1 35l-7.8-7.8 4.4-4.4 7.8 7.8zM21.3 59.2l28.6-28.6 7.8 7.8L29.1 67h-7.8v-7.8z"/></svg>
              </button>
              <button type="button" class="btn-del" title="Удалить" @click="delCell(cell.id)">
                <svg xmlns="http://www.w3.org/2000/svg" enable-background="new 0 0 24 24" viewBox="0 0 24 24"><path d="M19.8534546,19.1465454L12.7069092,12l7.1465454-7.1465454c0.1871948-0.1937256,0.1871948-0.5009155,0-0.6947021c-0.1918335-0.1986084-0.5083618-0.2041016-0.7069702-0.0122681l-7.1465454,7.1465454L4.8534546,4.1465454c-0.1937256-0.1871338-0.5009155-0.1871338-0.6947021,0C3.960144,4.3383789,3.9546509,4.6549072,4.1464844,4.8535156L11.2929688,12l-7.1464844,7.1464844c-0.09375,0.09375-0.1464233,0.2208862-0.1464233,0.3534546C4,19.776062,4.223877,19.999939,4.5,20c0.1326294,0.0001221,0.2598267-0.0526123,0.3534546-0.1465454l7.1464844-7.1464844l7.1465454,7.1465454C19.2401123,19.9474487,19.3673706,20.0001831,19.5,20c0.1325073-0.000061,0.2595825-0.0526733,0.3533325-0.1463623C20.048645,19.6583862,20.0487061,19.3417969,19.8534546,19.1465454z"/></svg>
              </button>
            </div>
          </div>
        </div>
      </div>

    </div>
    <div class="fixpanel">
      <span class="btn-content">
        <a href="javascript:;" class="btn-add" @click="modalManager('open')">
          <svg xmlns="http://www.w3.org/2000/svg" enable-background="new 0 0 32 32" viewBox="0 0 32 32"><switch><g><path d="M28,2H7C6.4,2,6,2.4,6,3v3H3C2.4,6,2,6.4,2,7v21c0,0.6,0.4,1,1,1h21c0.6,0,1-0.4,1-1v-3h3     c0.6,0,1-0.4,1-1V3C29,2.4,28.6,2,28,2z M23,27H4V8h3h16v16V27z M27,23h-2V7c0-0.6-0.4-1-1-1H8V4h19V23z"/><path d="M18,17h-4v-4c0-0.6-0.4-1-1-1s-1,0.4-1,1v4H8c-0.6,0-1,0.4-1,1s0.4,1,1,1h4v4c0,0.6,0.4,1,1,1s1-0.4,1-1     v-4h4c0.6,0,1-0.4,1-1S18.6,17,18,17z"/></g></switch></svg>
        </a>
      </span>
    </div>
  </div>
</template>

<script>
import {Fancybox} from "@fancyapps/ui";
import Modal from '@/components/Modal'


export default {
  data(){
    return {
      description_content: null,
      test: [],
      modal_open_status: false,
      cells: []
    }
  },
  compontents:{
    Modal
  },
  async mounted(){
    
    console.log(Modal)
  },
  async asyncData(context){
    try{
      const cells = await context.store.dispatch("trans/query", {
        action: "fetch"
      })
      //console.log(cells);
      return {
        cells
      }
    }catch(e){
      context.error(e);
    }
  },
  watch:{
    cells(){
      console.log(11)
    },
  },
  methods: {
    modalManager(act){
      console.log("index", act)
      switch(act){
        case "open":
          this.modal_open_status = true; break;
        case "close":
          this.modal_open_status = false; break;
      }
    },
    async delCell(id){
      var vm = this

      vm.$_.remove(vm.cells, {id})
      vm.cells = vm.$_.concat(vm.cells)
      console.log(vm.cells);
      //this.$set(this.cells)

      console.log(vm.cells, s, id)
      return;
      const req = await this.$axios.$post("/", {
        action: "delete",
        params: {id}
      })
      if(req.status === true){
        var s = this.$_.remove(this.cells, 'id='+id)
        console.log(this.cells, s)
        // this.cells.forEach((el, i)=>{
        //  console.log(i, el);

        // })
      }
        
    },
  },
  
}
</script>
