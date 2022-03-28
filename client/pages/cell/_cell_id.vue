<template>
  <div>
    <nuxt-link to="/test">Тест</nuxt-link>
    <div v-html="data">

    </div>
  </div>
</template>



<script>


export default {
  data(){
    return {

    }
  },
  async asyncData(context){
    try{
      const data = await context.store.dispatch("trans/query", { action: "wiki" })
      return {
        data
      }
    }catch(e){
      context.error(e);
    }
  },
  
}
</script>