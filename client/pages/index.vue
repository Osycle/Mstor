<template>
  <div class="index-wrapper">
    <div class="container-fluid">
      <nuxt-link to="/test">Тест</nuxt-link>
      <div class="cells">
        <div class="cell" v-for="(key) in 5" :key="key">
          <div class="cell-wrapper">
            <div class="date-content">
              {{ new Date(cells[0].date) | dateFormat('D MMMM YYYY')}}
            </div>
            <div class="img-content">
            </div>
            <div class="text-content">
              <span class="cell-title">{{cells[0].description}}</span>
              <span v-html="cells[0].description"></span>
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
      cells: [
        {
          date: 1642162712593,
          title: "Метохондрия",
          description: "Метохондрия Выделяет ATF, поглощает кислород, выделяет  угл. газ и воду"
        }
      ]
    }
  },
  async asyncData(context){
    try{
      
      const page_data = await context.store.dispatch("trans/fetchCells", {

          title: "test",
          description: "test",
          tags: "test"
        
      })
      //console.log(page_data);
      return {
        page_data
      }
    }catch(e){
      context.error(e);
    }
  },
}
</script>
