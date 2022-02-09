import Vue from 'vue';
//import "@/static/scss/_common.scss";
import VueFilterDateFormat from '@vuejs-community/vue-filter-date-format';

import VoerroTagsInput from '@voerro/vue-tagsinput';
Vue.component('tags-input', VoerroTagsInput);



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


Vue.filter('textLimit', (text, count)=>{ 
  if( text.length > count*1 ){
    text = text.substring(0, count )
    text = text+ " ...";
  }
	return text; 
})
