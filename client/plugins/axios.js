export default ({ $axios, app }) => {
  $axios.setHeader("Accept", "application/json");
  // $axios.setHeader("Authorization", "application/json");
  // $axios.setHeader("X-CSRF-Token", "FETCH");

  // $axios.defaults.xsrfHeaderName = 'x-csrftoken'
  // $axios.defaults.xsrfCookieName = 'csrftoken'
  // console.log($axios.defaults)
  if (app.$cookiz.get("token")) {
    $axios.setToken(app.$cookiz.get("token"), "Token");
  }
};
