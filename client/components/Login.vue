<template>
  <div>
    <h3>login</h3>
    
      <div><input type="text" name="login" placeholder="Login" v-model="username"></div><br>
      <input type="text" name="password" placeholder="Pass" v-model="pass">
      <button @click="send" style="color: white;" type="button">Отправить</button>
      <button @click="out" style="color: white;" type="button">Выйтинах</button>
  </div>
</template>
<script>
export default {
  data(){
    return{
      username:'jojo',
      pass: '11112222dddd'
    }
  },
  methods:{
    toFormData(object = {}) {
      const form = new FormData();

      try {
        Object.keys(object).map((objectKey) => {
          let pushFinally = true;
          let value = object[objectKey];
          if (objectKey === "remind_at") {
            value = value.toISOString();
          } else if (value instanceof File) {
            form.append(objectKey, value);
            pushFinally = false;
          } else if (Array.isArray(value)) {
            for (let i = 0; i < value.length; i++) {
              form.append(`${objectKey}[]`, value[i]);
            }
            pushFinally = false;
          } else if (typeof value === "object" && value !== null) {
            Object.keys(value).map((obKey, index) => {
              let v = value[obKey];
              form.append(`${objectKey}[${obKey}]`, v);
            });

            pushFinally = false;
          }

          if (pushFinally === true) {
            form.append(objectKey, value);
          }
        });
      } catch (error) {}

      return form;
    },
    async out(){
      this.$axios({
        method: "post",
        // data: this.toFormData({
        //   username: this.username,
        //   password: this.pass,
        // }),
        url: `http://localhost:8000/auth/token/logout`,
        headers: {
          "Content-Type": "multipart/form-data",
        },
      }).then((data)=>{
        this.$cookiz.remove("token");
        this.$axios.setToken(false);
      })
    },
    async send(){

      this.$axios({
        method: "post",
        data: this.toFormData({
          username: this.username,
          password: this.pass,
        }),
        url: `http://localhost:8000/auth/token/login`,
        headers: {
          "Content-Type": "multipart/form-data",
        },
      }).then((data)=>{
        
        const token = data.data.auth_token;
        //SET COOKIE
        this.$cookiz.set("token", token, {
          // maxAge: expires_at,
          path: "/",
        });
        //SET HEADER
        this.$axios.setToken(token, "Token");
      })
      
 
    }
  }
}
</script>