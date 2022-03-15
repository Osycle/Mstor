
export const actions = {
  
  async query(context, params){
    try {
      //console.log("this.$axios ", axios);
      const data = await this.$axios.$post("/handler.py", params);
      return data;
    }catch(e){
      throw e;
    }
  },
}