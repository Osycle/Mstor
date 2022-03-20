
export const actions = {
  
  //"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
  //"Content-Type": "text/plain; charset=UTF-8"

  async query(context, params){
    try {
      const data = await this.$axios.$post("/handler.py", {action: "fetch_cells"});
      return data;
    }catch(e){
      throw e;
    }
  },
}