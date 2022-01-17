
export const actions = {
  async fetchCells(context, params){
    try {
      //console.log("context other, ", context);
      const data = await this.$axios.$post("http://mstor.server",  params, {
          headers: {
            //Accept: 'application/x-www-form-urlencoded',
            'Content-Type': 'application/x-www-form-urlencoded'
          }
        
      });
      return data;
    }catch(e){
      throw e;
    }
  }
}