<template>
  <div class="index-wrapper">
    <div class="container-fluid">
      <nuxt-link to="/test">Тест</nuxt-link>
      <div class="cells">
        <div class="cell" v-for="(cell, key) in cells" :key="key" @click="ins">
          <div class="cell-wrapper">
            <div class="date-content">
              {{ new Date(cell.date_time) | dateFormat('D MMMM YYYY')}}
            </div>
            <div class="img-content">
            </div>
            <div class="text-content">
              <span class="cell-title">{{cell.title}}</span>
              <span v-html="cell.description"></span>
            </div>
            <div class="btn-content">
              <button type="button" class="btn-edit" title="Редактировать">
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 101 101"><path d="M82.2 79.2H18.8c-1.3 0-2.4 1.1-2.4 2.4s1.1 2.4 2.4 2.4h63.4c1.3 0 2.4-1.1 2.4-2.4s-1.1-2.4-2.4-2.4zM16.5 58.2l-.1 11.3c0 .6.2 1.3.7 1.7.5.4 1.1.7 1.7.7l11.3-.1c.6 0 1.2-.3 1.7-.7l38.8-38.8c.9-.9.9-2.5 0-3.4L59.4 17.7c-.9-.9-2.5-.9-3.4 0l-7.8 7.8-31 31c-.5.5-.7 1.1-.7 1.7zm49-27.6L61.1 35l-7.8-7.8 4.4-4.4 7.8 7.8zM21.3 59.2l28.6-28.6 7.8 7.8L29.1 67h-7.8v-7.8z"/></svg>
              </button>
            </div>
          </div>
        </div>
      </div>
      <div class="">
        <div class="addcell" id="addcell">
          <div class="title-content">
            Добавить
          </div>
          <wysiwyg v-model="myHTML" />
        </div>
      </div>
    </div>
    <div class="fixpanel">
      <span class="btn-content">
        <a href="#addcell" class="btn-add" data-fancybox>
          <svg xmlns="http://www.w3.org/2000/svg" enable-background="new 0 0 32 32" viewBox="0 0 32 32"><switch><g><path d="M28,2H7C6.4,2,6,2.4,6,3v3H3C2.4,6,2,6.4,2,7v21c0,0.6,0.4,1,1,1h21c0.6,0,1-0.4,1-1v-3h3     c0.6,0,1-0.4,1-1V3C29,2.4,28.6,2,28,2z M23,27H4V8h3h16v16V27z M27,23h-2V7c0-0.6-0.4-1-1-1H8V4h19V23z"/><path d="M18,17h-4v-4c0-0.6-0.4-1-1-1s-1,0.4-1,1v4H8c-0.6,0-1,0.4-1,1s0.4,1,1,1h4v4c0,0.6,0.4,1,1,1s1-0.4,1-1     v-4h4c0.6,0,1-0.4,1-1S18.6,17,18,17z"/></g></switch></svg>
        </a>
      </span>
    </div>
  </div>
</template>

<script>



export default {
  data(){
    return {
      myHTML: null,
      test: [],
      // cells: [
      //   {
      //     date: 1642162712593,
      //     title: "Метохондрия",
      //     description: "Метохондрия Выделяет ATF, поглощает кислород, выделяет  угл. газ и воду"
      //   }
      // ]
    }
  },
  async mounted(){

    // this.selectComplectations = await this.$axios.$post("http://mstor.server", {ols:122},{
    //   //'Content-Type': 'application/json',

    // });
    // console.log(this.selectComplectations, "created")
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
  methods: {
    async ins(){
      return;
      this.test = await this.$axios.$post("/", {
        action: "insert",
        params: {
          title: "new Title",
          description: "new Desc",
          tags: "new Tags"
        }
      })
      console.log(this.test);
    }
  }
}
</script>
