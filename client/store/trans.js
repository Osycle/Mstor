
export const actions = {
  
  async query(context, params){
    try {
      const data = await this.$axios.$post("/cgi-bin/handler.py", 
      {action: "fetch"},
      //'action="fetch"',
      {
        headers: {
          //"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
          //"Content-Type": "text/plain; charset=UTF-8"
        }
      });
      return data;
    }catch(e){
      throw e;
    }
  },
}