<template>
      <div class="index-wrapper">
      
      <div class="tags-main hide">
        <div class="tags-items">
          <div v-for="(tag, key) in all_tags" :key="key" v-if="key<8" class="tag-item">
            <span role="button" class="tag-link">
              {{tag.name}}
            </span>
          </div>
        </div>
      </div>
      <div class="container-p">
        <div class="main-wrapper">
          <div class="cells-content hide">
            <div class="cells" v-if="cells.length">
              <div class="cell a-scale" v-for="(cell, key) in cells" :key="key" :style="'--i: '+key">
                <div class="tags-content">
                  <span v-for="(item, key) in cell.tags" :key="key" class="tags-item">
                    {{item.name}}
                  </span>
                </div>
                <div class="cell-wrapper">
                  <div class="date-content">
                    {{ new Date(cell.time_create) | dateFormat('D MMMM YYYY')}}
                  </div>
                  <div class="content">
                    <!-- <nuxt-link :to="'/cell/'+cell.id">Далее</nuxt-link> -->
                    <div v-html="parse_text(cell.content)" class="content-wrapper"></div>
                  </div>
                </div>
                <div class="btn-content">
                  <button type="button" class="btn btn-views" title="Больше">
                    <svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 32 32"><path d="m 16,7.980468 c -3.78678,0 -7.22322,1.04576 -9.76953,2.80859 C 3.68416,12.551898 2,15.099848 2,17.980468 a 1.0000999,1.0000999 0 1 0 2,0 c 0,-2.10538 1.21595,-4.05621 3.36914,-5.54687 2.15319,-1.49067 5.21564,-2.45313 8.63086,-2.45313 3.41522,0 6.47962,0.96246 8.63281,2.45313 C 26.786,13.924258 28,15.875088 28,17.980468 a 1.0000999,1.0000999 0 1 0 2,0 c 0,-2.88062 -1.6822,-5.42857 -4.22852,-7.19141 C 23.22517,9.026228 19.78678,7.980468 16,7.980468 Z" color="currentColor" font-family="sans-serif" font-weight="400" overflow="visible" style="line-height:normal;font-variant-ligatures:normal;font-variant-position:normal;font-variant-caps:normal;font-variant-numeric:normal;font-variant-alternates:normal;font-feature-settings:normal;text-indent:0;text-align:start;text-decoration-line:none;text-decoration-style:solid;text-decoration-color:currentColor;text-transform:none;text-orientation:mixed;shape-padding:0;isolation:auto;mix-blend-mode:normal"/><path d="m 16,13.980468 c -2.74958,0 -5,2.25042 -5,5 0,2.74958 2.25042,5 5,5 2.74958,0 5,-2.25042 5,-5 0,-2.74958 -2.25042,-5 -5,-5 z m 0,2 c 1.6687,0 3,1.3313 3,3 0,1.6687 -1.3313,3 -3,3 -1.6687,0 -3,-1.3313 -3,-3 0,-1.6687 1.3313,-3 3,-3 z" color="currentColor" font-family="sans-serif" font-weight="400" overflow="visible" style="line-height:normal;font-variant-ligatures:normal;font-variant-position:normal;font-variant-caps:normal;font-variant-numeric:normal;font-variant-alternates:normal;font-feature-settings:normal;text-indent:0;text-align:start;text-decoration-line:none;text-decoration-style:solid;text-decoration-color:currentColor;text-transform:none;text-orientation:mixed;shape-padding:0;isolation:auto;mix-blend-mode:normal"/></svg>
                  </button>
                  <button type="button" class="btn btn-edit" title="Редактировать" @click="editCell(cell)">
                    <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24"><path d="M17.864 3.60051C17.4735 3.20999 16.8403 3.20999 16.4498 3.60051L15.0356 5.01472 19.2782 9.25736 20.6924 7.84315C21.0829 7.45263 21.0829 6.81946 20.6924 6.42894L17.864 3.60051zM17.864 10.6716L13.6213 6.42894 4.72185 15.3284C4.53431 15.516 4.42896 15.7703 4.42896 16.0355L4.42896 18.864C4.42895 19.4163 4.87667 19.864 5.42896 19.864H8.25738C8.5226 19.864 8.77695 19.7586 8.96449 19.5711L17.864 10.6716z"/></svg>
                  </button>
                  <button type="button" class="btn btn-del" title="Удалить" @click="delCell(cell)">
                    <svg xmlns="http://www.w3.org/2000/svg" enable-background="new 0 0 24 24" viewBox="0 0 24 24"><path d="M19.8534546,19.1465454L12.7069092,12l7.1465454-7.1465454c0.1871948-0.1937256,0.1871948-0.5009155,0-0.6947021c-0.1918335-0.1986084-0.5083618-0.2041016-0.7069702-0.0122681l-7.1465454,7.1465454L4.8534546,4.1465454c-0.1937256-0.1871338-0.5009155-0.1871338-0.6947021,0C3.960144,4.3383789,3.9546509,4.6549072,4.1464844,4.8535156L11.2929688,12l-7.1464844,7.1464844c-0.09375,0.09375-0.1464233,0.2208862-0.1464233,0.3534546C4,19.776062,4.223877,19.999939,4.5,20c0.1326294,0.0001221,0.2598267-0.0526123,0.3534546-0.1465454l7.1464844-7.1464844l7.1465454,7.1465454C19.2401123,19.9474487,19.3673706,20.0001831,19.5,20c0.1325073-0.000061,0.2595825-0.0526733,0.3533325-0.1463623C20.048645,19.6583862,20.0487061,19.3417969,19.8534546,19.1465454z"/></svg>
                  </button>
                </div>
              </div>
            </div>
            <div v-else class="cells-empty">
              <div>
                <p>Ничего не найдено</p>
              </div>
            </div>
          </div>
          <div class="well">
            <div class="well-wrapper">
              <masonry-wall :items="cells" :ssr-columns="1" :column-width="250" :gap="10">
                <template #default="{ item }">
                  <div class="cell" @click="cell_select(item)">
                    <div class="cell-wrapper">
                      <div class="date-content hide">
                        {{ new Date(item.time_create) | dateFormat('D MMMM YYYY')}}
                      </div>
                      <div class="content">
                        <div v-html="parse_text(item.content)" class="content-wrapper"></div>
                      </div>
                    </div>                
                  </div>
                </template>
              </masonry-wall>
            </div>
          </div>
        </div>

      </div>
      <Bar 
        :current_cell="current_cell" 
        @cell_append="cell_append"
        @cell_update="cell_update" 
        @cell_remove="cell_remove"
        />
      <div class="fixpanel">
        <div id="search" class="search hide">
          <div class="search-content">
            <input type="search" name="search" @keyup="search(search_query, $event)" v-model="search_query">
            <div class="icon-content">
              <svg xmlns="http://www.w3.org/2000/svg" width="22" height="22" viewBox="0 0 22 22"><path d="M19.7555474,18.6065254 L16.3181544,15.2458256 L16.3181544,15.2458256 L16.2375905,15.1233001 C16.0877892,14.9741632 15.8829641,14.8901502 15.6691675,14.8901502 C15.4553709,14.8901502 15.2505458,14.9741632 15.1007444,15.1233001 L15.1007444,15.1233001 C12.1794834,17.8033337 7.6781476,17.94901 4.58200492,15.4637171 C1.48586224,12.9784243 0.75566836,8.63336673 2.87568494,5.31016931 C4.99570152,1.9869719 9.30807195,0.716847023 12.9528494,2.34213643 C16.5976268,3.96742583 18.4438102,7.98379036 17.2670181,11.7275931 C17.182269,11.9980548 17.25154,12.2921761 17.4487374,12.4991642 C17.6459348,12.7061524 17.9410995,12.794561 18.223046,12.7310875 C18.5049924,12.667614 18.7308862,12.4619014 18.8156353,12.1914397 L18.8156353,12.1914397 C20.2223941,7.74864367 18.0977423,2.96755391 13.8161172,0.941057725 C9.53449216,-1.08543846 4.38083811,0.250823958 1.68905427,4.08541671 C-1.00272957,7.92000947 -0.424820906,13.1021457 3.0489311,16.2795011 C6.5226831,19.4568565 11.8497823,19.6758854 15.5841278,16.7948982 L18.6276529,19.7705177 C18.9419864,20.0764941 19.4501654,20.0764941 19.764499,19.7705177 C20.0785003,19.4602048 20.0785003,18.9605974 19.764499,18.6502845 L19.764499,18.6502845 L19.7555474,18.6065254 Z"/></svg>
            </div>
          </div>
        </div>
        <span class="btn-content">
          <a href="javascript:;" class="flex ai-center" @click="current_cell = null">
            <span class="btn-add">
              <svg xmlns="http://www.w3.org/2000/svg" enable-background="new 0 0 32 32" viewBox="0 0 32 32"><switch><g><path d="M28,2H7C6.4,2,6,2.4,6,3v3H3C2.4,6,2,6.4,2,7v21c0,0.6,0.4,1,1,1h21c0.6,0,1-0.4,1-1v-3h3     c0.6,0,1-0.4,1-1V3C29,2.4,28.6,2,28,2z M23,27H4V8h3h16v16V27z M27,23h-2V7c0-0.6-0.4-1-1-1H8V4h19V23z"/><path d="M18,17h-4v-4c0-0.6-0.4-1-1-1s-1,0.4-1,1v4H8c-0.6,0-1,0.4-1,1s0.4,1,1,1h4v4c0,0.6,0.4,1,1,1s1-0.4,1-1     v-4h4c0.6,0,1-0.4,1-1S18.6,17,18,17z"/></g></switch></svg>
            </span>
          </a>    
        </span>
      </div>
    </div>
</template>

<script>
import {Fancybox} from "@fancyapps/ui";
import Modal from '@/components/Modal'
import Bar from '@/components/Bar'

// import { createApp } from 'vue'
// import MasonryWall from '@yeger/vue-masonry-wall'
// const app = createApp()
// app.use(MasonryWall)

export default {
  data(){
    return {
      items: [
        { title: 'First', description: 'The first item.' },
        { title: 'Second', description: 'The second item.' },
      ],
      description_content: null,
      test: [],
      data: null,
      cells: [],
      current_cell: null,
      cells_init: [],
      search_query: "",
      all_tags: [],
    }
  },
  compontents:{
    Modal,
    Bar,
  },
  async mounted(){
    window.vm_index = this;    
    $(document).off("click.more", ".btn-views")
    $(document).on("click.more", ".btn-views", function(){
      $(this).closest(".cell").find(".content-detail").toggleClass("active");
    })
    var owl = $('.owl-carousel');

  },
  async created(){
    const data = await this.$axios.$get("cells/", { action: "fetch_cells" })
    // const data = await context.store.dispatch("trans/query", { action: "fetch_cells" })
      // console.log(data)
      this.cells = data.cells
      this.cells_init = data.cells
      this.all_tags = data.tags
      
  },
  watch:{
    cells(){
      //console.log(11)
    },
  },
  filters: {

  },
  methods: {
    parse_media(string){
      const pattern_media = /<iframe.+?><\/iframe>|<img.+?>/gim;
      const pattern_iframe = /<iframe.+?><\/iframe>/gim;
      const pattern_img = /<img.+?>/gim;
      let media = string.match(pattern_media)
      let out_content = ""
      if(!media)
        return "";

      media.forEach(function(text_path, i){
        pattern_iframe.lastIndex = 0
        pattern_img.lastIndex = 0
        let new_content = "";
        let link = text_path.match(/src=\"(.*?)\"/im)[1];
        if(pattern_iframe.test(text_path)){
          if(/youtube/.test(text_path)){
            var code = text_path.match(/embed\/(.+)\?/im)[1]
            new_content = `
              <a href="${link}" data-fancybox class='cell-yt-link cell-media-link content-iframe'>
                <img src="https://i.ytimg.com/vi/${code}/hqdefault.jpg">
              </a>
            `
          }else{
            new_content = `
              <a href="${link}" data-fancybox class='cell-media-link content-iframe'>
                <video src="${link}">
              </a>
            `
          }
        }
        if(pattern_img.test(text_path)){
          new_content = `
            <a href="${link}" data-fancybox class='cell-media-link content-img'>
              <img src="${link}">
            </a>
          `
        }
        out_content += new_content
      })
      return `
        <div class="media-content">
          <div class="wrapper">
            ${out_content}
          </div>
        </div>
      `;
    },
    parse_links(string){
      const pattern_a = /<a.+?>/gim;
      let out_content = ""
      let links = string.match(pattern_a);
      if(!links)
        return "";
      links.forEach(function(text_path){
        pattern_a.lastIndex = 0
        let link = text_path.match(/href=\"(.*?)\"/im)[1]
        let new_content = `
          <a href="${link}" target='_blank'>
            ${link}
          </a>
        `
        out_content += new_content
      })
      return "<div class='links-content'>"+out_content+"</div>";
    },
    parse_text(string){
      
      let tpl_links = this.parse_links(string);
      let tpl_media = this.parse_media(string);
      // string = $(string).text()
      // string = string.replace(/<p><br><\/p>|<p><\/p>|<a.+?>|<iframe.+?><\/iframe>|<img.+?>/gim, " ");
      // string = string.replace(/<p><br><\/p>|<p><\/p>/gim, "");
      // console.log(string)
      string = "<div class='text-content'>"+string+"</div>"
      string += `
        <div class="content-detail">
          ${tpl_links}
          ${tpl_media}
        </div>`


      
      // string = newstr+string
      return string;
    },
    cell_select(cell){
      this.current_cell = cell
    },
    cell_append(cell){
      console.log(cell, 'Я вызвался')
      this.cells.push(cell);
    },
    cell_remove(cell_id){
      this.$_.remove(this.cells, {id: cell_id})
      this.cells = this.$_.concat(this.cells)
    },
    cell_update(cell){
       var index = this.$_.findIndex(this.cells, {'id': cell.id});
       this.cells[index] = cell
       this.cells = this.$_.concat(this.cells)
    },

    async search(query, event){
      var vm = this
      // console.log(query, event)
      if(query.length < 3){
        this.cells = this.cells_init
        return;
      }

      if(window.searchTimeout)
        clearTimeout(window.searchTimeout)
        
      window.searchTimeout = setTimeout(async ()=>{
        const response = await vm.$axios.$post("/handler.py", {
          action: "search",
          query,
        })
        if(response.status == true){
          vm.cells = response.cells
        }
      }, 300);
    }
  },
  
}
</script>