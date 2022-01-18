
export const actions = {
  async fetchCells(context, params){
    try {
      //console.log("this.$axios ", this);
      const data = await this.$axios.$post("http://mstor.server",  params, {
          // headers: {
            
          //   Accept: 'application/x-www-form-urlencoded',
          //   'Content-Type': 'application/x-www-form-urlencoded'
          // }
        
      });
      return data;
    }catch(e){
      throw e;
    }
  }
}