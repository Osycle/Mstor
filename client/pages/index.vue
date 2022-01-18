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
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>



export default {
  data(){
    return {
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
      console.log(cells);
      return {
        cells
      }
    }catch(e){
      context.error(e);
    }
  },
  methods: {
    async ins(){
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
