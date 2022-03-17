
export const actions = {
  
  async query(context, params){
    try {
      const data = await this.$axios.$post("/cgi-bin/handler.py", {data:8888});
      return data;
    }catch(e){
      throw e;
    }
  },
}