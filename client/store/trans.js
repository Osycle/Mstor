
export const actions = {
  
  async query(context, params){
    this.$axios.defaults.headers.post['Content-Type'] ='application/json;charset=utf-8';
    this.$axios.defaults.headers.post['Access-Control-Allow-Origin'] = '*';
    try {
      //console.log("this.$axios ", axios);
      const data = await this.$axios.$get("/handler.py", params);
      return data;
    }catch(e){
      throw e;
    }
  },
}