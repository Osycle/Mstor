
export const actions = {
  
  async query(context, params){
    try {
      //console.log("this.$axios ", axios);
      const data = await this.$axios.$post("/cgi-bin/handler.py", {data:8888});
      return data;
    }catch(e){
      throw e;
    }
  },
}