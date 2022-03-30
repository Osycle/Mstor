<template>
  <div class="index-wrapper">
    <Modal 
      @cell_append="cell_append" 
      @cell_update="cell_update" 
      :all_tags="all_tags"
      v-if="$store.state.modal.status"/>
    <div class="container-fluid">
      <div class="main-wrapper">
        <div class="cells-content">
          <div class="cells">
            <div class="cell" v-for="(cell, key) in cells" :key="key">
              <div class="tags-content">
                <span v-for="(item, key) in cell.tags" :key="key" class="tags-item">
                  {{item.name}}
                </span>
              </div>
              <div class="cell-wrapper">
                <div class="date-content">
                  {{ new Date(cell.date_time*1000) | dateFormat('D MMMM YYYY')}}
                </div>
                <div class="text-content">
                  <!-- <nuxt-link :to="'/cell/'+cell.id">Далее</nuxt-link> -->
                  <div v-html="parseText(cell.description)"></div>
                </div>
              </div>
              <div class="btn-content">
                <button type="button" class="btn-edit" title="Редактировать" @click="editCell(cell)">
                  <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 101 101"><path d="M82.2 79.2H18.8c-1.3 0-2.4 1.1-2.4 2.4s1.1 2.4 2.4 2.4h63.4c1.3 0 2.4-1.1 2.4-2.4s-1.1-2.4-2.4-2.4zM16.5 58.2l-.1 11.3c0 .6.2 1.3.7 1.7.5.4 1.1.7 1.7.7l11.3-.1c.6 0 1.2-.3 1.7-.7l38.8-38.8c.9-.9.9-2.5 0-3.4L59.4 17.7c-.9-.9-2.5-.9-3.4 0l-7.8 7.8-31 31c-.5.5-.7 1.1-.7 1.7zm49-27.6L61.1 35l-7.8-7.8 4.4-4.4 7.8 7.8zM21.3 59.2l28.6-28.6 7.8 7.8L29.1 67h-7.8v-7.8z"/></svg>
                </button>
                <button type="button" class="btn-del" title="Удалить" @click.once="delCell(cell)">
                  <svg xmlns="http://www.w3.org/2000/svg" enable-background="new 0 0 24 24" viewBox="0 0 24 24"><path d="M19.8534546,19.1465454L12.7069092,12l7.1465454-7.1465454c0.1871948-0.1937256,0.1871948-0.5009155,0-0.6947021c-0.1918335-0.1986084-0.5083618-0.2041016-0.7069702-0.0122681l-7.1465454,7.1465454L4.8534546,4.1465454c-0.1937256-0.1871338-0.5009155-0.1871338-0.6947021,0C3.960144,4.3383789,3.9546509,4.6549072,4.1464844,4.8535156L11.2929688,12l-7.1464844,7.1464844c-0.09375,0.09375-0.1464233,0.2208862-0.1464233,0.3534546C4,19.776062,4.223877,19.999939,4.5,20c0.1326294,0.0001221,0.2598267-0.0526123,0.3534546-0.1465454l7.1464844-7.1464844l7.1465454,7.1465454C19.2401123,19.9474487,19.3673706,20.0001831,19.5,20c0.1325073-0.000061,0.2595825-0.0526733,0.3533325-0.1463623C20.048645,19.6583862,20.0487061,19.3417969,19.8534546,19.1465454z"/></svg>
                </button>
              </div>
            </div>
          </div>
        </div>
        <div class="tags-main">
          <div class="wrapper">
            <div class="tags-items">
              <div v-for="(tag, key) in all_tags" :key="key" class="tag-item" role="button">
                <span>{{tag.name}}</span>
              </div>
            </div>
          </div>
        </div>
      </div>

    </div>
    <div class="fixpanel">
      <div id="search" class="search">
        <div class="search-content">
          <input type="text" name="">
          <div class="icon-content">
            <svg xmlns="http://www.w3.org/2000/svg" width="22" height="22" viewBox="0 0 22 22"><path d="M19.7555474,18.6065254 L16.3181544,15.2458256 L16.3181544,15.2458256 L16.2375905,15.1233001 C16.0877892,14.9741632 15.8829641,14.8901502 15.6691675,14.8901502 C15.4553709,14.8901502 15.2505458,14.9741632 15.1007444,15.1233001 L15.1007444,15.1233001 C12.1794834,17.8033337 7.6781476,17.94901 4.58200492,15.4637171 C1.48586224,12.9784243 0.75566836,8.63336673 2.87568494,5.31016931 C4.99570152,1.9869719 9.30807195,0.716847023 12.9528494,2.34213643 C16.5976268,3.96742583 18.4438102,7.98379036 17.2670181,11.7275931 C17.182269,11.9980548 17.25154,12.2921761 17.4487374,12.4991642 C17.6459348,12.7061524 17.9410995,12.794561 18.223046,12.7310875 C18.5049924,12.667614 18.7308862,12.4619014 18.8156353,12.1914397 L18.8156353,12.1914397 C20.2223941,7.74864367 18.0977423,2.96755391 13.8161172,0.941057725 C9.53449216,-1.08543846 4.38083811,0.250823958 1.68905427,4.08541671 C-1.00272957,7.92000947 -0.424820906,13.1021457 3.0489311,16.2795011 C6.5226831,19.4568565 11.8497823,19.6758854 15.5841278,16.7948982 L18.6276529,19.7705177 C18.9419864,20.0764941 19.4501654,20.0764941 19.764499,19.7705177 C20.0785003,19.4602048 20.0785003,18.9605974 19.764499,18.6502845 L19.764499,18.6502845 L19.7555474,18.6065254 Z"/></svg>
          </div>
        </div>
      </div>
      <span class="btn-content">
        <a href="javascript:;" class="btn-add" @click="$store.commit('modal/open')">
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
      data: null,
      cells: [],
      all_tags: []
    }
  },
  compontents:{
    Modal
  },
  async mounted(){
    window.vm_index = this;
  },
  async asyncData(context){
    try{
      const data = await context.store.dispatch("trans/query", { action: "fetch_cells" })
      return {
        cells: data.cells,
        all_tags: data.tags,
      }
    }catch(e){
      context.error(e);
    }
  },
  watch:{
    cells(){
      //console.log(11)
    },
  },
  filters: {

  },
  methods: {

    parseText(string){
      return string;
      window.pattern_link = /(https?:\/\/|ftps?:\/\/|www\.)((?![.,?!;:()]*(\s|$))[^\s]){2,}/gim
      string = string.replace(pattern_link, function(a){
        console.log(11111111,a)
        return "<a href='#'>"+a+"</a>"
      })
      var string_match = string.match(pattern_link)
      return string;
    },
    cell_append(cell){
      this.cells.push(cell);
    },
    cell_remove(cell){
      this.$_.remove(this.cells, {id: cell.id})
      this.cells = this.$_.concat(this.cells)
    },
    cell_update(cell){
       var index = this.$_.findIndex(this.cells, {'id': cell.id});
       this.cells[index] = cell
       console.log(this.cells, index);
    },
    async delCell(cell){
      var vm = this
      const response = await this.$axios.$post("/handler.py", {
        action: "delete_cell",
        cell_id: cell.id
      })
      if(response.status == true){
        this.cell_remove(cell)
      }
    },
    async editCell(cell){
      var vm = this
      console.log(cell)
      this.$store.commit("modal/open", cell)
    },
  },
  
}
</script>
