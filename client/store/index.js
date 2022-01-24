import Vue from 'vue';
import VueFilterDateFormat from '@vuejs-community/vue-filter-date-format';
import wysiwyg from "vue-wysiwyg";

Vue.use(wysiwyg, {
  // { [module]: boolean (set true to hide) }
  hideModules: { "bold": false },
 
  // you can override icons too, if desired
  // just keep in mind that you may need custom styles in your application to get everything to align
  //iconOverrides: { "bold": "<i class="your-custom-icon"></i>" },
 
  // if the image option is not set, images are inserted as base64
  // image: {
  //   uploadURL: "/api/myEndpoint",
  //   dropzoneOptions: {}
  // },
 
  // limit content height if you wish. If not set, editor size will grow with content.
  maxHeight: "500px"
});
Vue.use(VueFilterDateFormat, {
  dayOfWeekNames: [
    'Воскресенье', 'Понедельник', 'Вторник', 'Среда', 'Четверг',
    'Пятница', 'Суббота'
  ],
  dayOfWeekNamesShort: [
    'Su', 'Mo', 'Tu', 'We', 'Tr', 'Fr', 'Sa'
  ],
  monthNames: [
    'Января', 'Февраля', 'Марта', 'Апреля', 'Мая', 'Июня', 'Июля', 'Августа', 'Сентября', 'Октября', 'Ноября', 'Декабря'
  ],
  monthNamesShort: [
    'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
    'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'
  ],
  // Timezone offset, in minutes (0 - UTC, 180 - Russia, undefined - current)
  timezone: 5
});

Vue.filter('spaceBetweenNum', (price)=>{ 
	price += "";
	var pattern = /(-?\d+)(\d{3})/;
	while (pattern.test(price))
		price = price.replace(pattern, "$1 $2");
	return price; 
})
