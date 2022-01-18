
export const actions = {
  async query(context, params){
    try {
      //console.log("this.$axios ", this);
      const data = await this.$axios.$post("/", params);
      return data;
    }catch(e){
      throw e;
    }
  },
}