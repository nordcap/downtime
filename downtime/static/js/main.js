//определение текущей даты. 
//по непонятной причине в шаблоне компонента current-date должен быть 
//определенный формат даты YYYY-MM-DD
//такой YYYY-M-D  или иной другой уже не подходит.
var curDate = new Date()
var year = curDate.getFullYear().toString()
var month = (curDate.getMonth() + 1).toString()
var day = curDate.getDate().toString()

if (month.length == 1) {
    month = "0" + month
}
if (day.length == 1) {
    day = "0" + day
}


//компонент для определения текущей даты
Vue.component('current-date', {

    data: function () {
        return {
            currentDate: year + "-" + month + "-" + day
        }
    },
    template: '<input type="date" v-model="currentDate">'

})


//компонент ввода времени простоя
Vue.component('loose-time', {
    props: ['title', 'value'],
    template: '<input type="time" v-bind:value="value" v-bind:name="title">'
})

//компонент для ввода комментариев
Vue.component('comment', {
    props: ['value'],
    template: '<input type="text" v-bind:value="value">'

})


new Vue({el: "#current-date"})


var app = new Vue({
    el: '#app',
    delimiters: ['[[', ']]'],
    data: {
        objectlist: [
            {
                id: 1,
                obj: "ДСУ-1",
                smena1: {
                    types: [
                        {
                            type: "ППР",
                            amount: "01:00"
                        },
                        {
                            type: "ТР",
                            amount: "02:00"
                        },
                        {
                            type: "СР",
                            amount: "03:00"
                        },
                        {
                            type: "КР",
                            amount: "04:00"
                        },
                        {
                            type: "ТО",
                            amount: "05:00"
                        },
                        {
                            type: "ВР",
                            amount: "05:00"
                        },
                        {
                            type: "П",
                            amount: "07:00"
                        },
                        {
                            type: "ОЗ",
                            amount: "08:00"
                        },
                        {
                            type: "ОТ",
                            amount: "09:00"
                        },
                        {
                            type: "ОЗЧ",
                            amount: "10:00"
                        },
                        {
                            type: "И",
                            amount: "11:00"
                        },
                        {

                            type: "ПУ",
                            amount: "12:00"
                        },
                        {

                            type: "ОБ",
                            amount: "13:00"
                        },
                        {

                            type: "НЗС",
                            amount: "14:00"
                        },
                        {

                            type: "З",
                            amount: "15:00"
                        },
                        {

                            type: "Ч",
                            amount: "16:00"
                        },
                        {

                            type: "Р",
                            amount: "17:00"
                        },
                        {

                            type: "А",
                            amount: "18:00"
                        }


                    ],
                    comment1: "описание 1 ДСУ-1"
                },
                smena2: {
                    types: [
                        {
                            type: "ППР",
                            amount: "01:00"
                        },
                        {
                            type: "ТР",
                            amount: "02:00"
                        },
                        {
                            type: "СР",
                            amount: "03:00"
                        },
                        {
                            type: "КР",
                            amount: "04:00"
                        },
                        {
                            type: "ТО",
                            amount: "05:00"
                        },
                        {
                            type: "ВР",
                            amount: "05:00"
                        },
                        {
                            type: "П",
                            amount: "07:00"
                        },
                        {
                            type: "ОЗ",
                            amount: "08:00"
                        },
                        {
                            type: "ОТ",
                            amount: "09:00"
                        },
                        {
                            type: "ОЗЧ",
                            amount: "10:00"
                        },
                        {
                            type: "И",
                            amount: "11:00"
                        },
                        {

                            type: "ПУ",
                            amount: "12:00"
                        },
                        {

                            type: "ОБ",
                            amount: "13:00"
                        },
                        {

                            type: "НЗС",
                            amount: "14:00"
                        },
                        {

                            type: "З",
                            amount: "15:00"
                        },
                        {

                            type: "Ч",
                            amount: "16:00"
                        },
                        {

                            type: "Р",
                            amount: "17:00"
                        },
                        {

                            type: "А",
                            amount: "18:00"
                        }
                    ],
                    comment2: "описание 2 ДСУ-1"
                }
            },
            {
                id: 2,
                obj: "ДСУ-2",
                smena1: {
                    types: [
                        {
                            type: "ППР",
                            amount: "01:00"
                        },
                        {
                            type: "ТР",
                            amount: "02:00"
                        },
                        {
                            type: "СР",
                            amount: "03:00"
                        },
                        {
                            type: "КР",
                            amount: "04:00"
                        },
                        {
                            type: "ТО",
                            amount: "05:00"
                        },
                        {
                            type: "ВР",
                            amount: "05:00"
                        },
                        {
                            type: "П",
                            amount: "07:00"
                        },
                        {
                            type: "ОЗ",
                            amount: "08:00"
                        },
                        {
                            type: "ОТ",
                            amount: "09:00"
                        },
                        {
                            type: "ОЗЧ",
                            amount: "10:00"
                        },
                        {
                            type: "И",
                            amount: "11:00"
                        },
                        {

                            type: "ПУ",
                            amount: "12:00"
                        },
                        {

                            type: "ОБ",
                            amount: "13:00"
                        },
                        {

                            type: "НЗС",
                            amount: "14:00"
                        },
                        {

                            type: "З",
                            amount: "15:00"
                        },
                        {

                            type: "Ч",
                            amount: "16:00"
                        },
                        {

                            type: "Р",
                            amount: "17:00"
                        },
                        {

                            type: "А",
                            amount: "18:00"
                        }


                    ],
                    comment1: "описание 1 ДСУ-2"
                },
                smena2: {
                    types: [
                        {
                            type: "ППР",
                            amount: "01:00"
                        },
                        {
                            type: "ТР",
                            amount: "02:00"
                        },
                        {
                            type: "СР",
                            amount: "03:00"
                        },
                        {
                            type: "КР",
                            amount: "04:00"
                        },
                        {
                            type: "ТО",
                            amount: "05:00"
                        },
                        {
                            type: "ВР",
                            amount: "05:00"
                        },
                        {
                            type: "П",
                            amount: "07:00"
                        },
                        {
                            type: "ОЗ",
                            amount: "08:00"
                        },
                        {
                            type: "ОТ",
                            amount: "09:00"
                        },
                        {
                            type: "ОЗЧ",
                            amount: "10:00"
                        },
                        {
                            type: "И",
                            amount: "11:00"
                        },
                        {

                            type: "ПУ",
                            amount: "12:00"
                        },
                        {

                            type: "ОБ",
                            amount: "13:00"
                        },
                        {

                            type: "НЗС",
                            amount: "14:00"
                        },
                        {

                            type: "З",
                            amount: "15:00"
                        },
                        {

                            type: "Ч",
                            amount: "16:00"
                        },
                        {

                            type: "Р",
                            amount: "17:00"
                        },
                        {

                            type: "А",
                            amount: "18:00"
                        }
                    ],
                    comment2: "описание 2 ДСУ-2"
                }
            }
        ]
    }

})