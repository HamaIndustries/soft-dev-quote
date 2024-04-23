<template>
    <h1 class="QuoteHeader">Quote History</h1>
    <table :key="loaded">
        <thead>
            <tr class="table-row">
                <th class = "table-column_item table-header_item"
                    v-for = "col in cols"
                    :key = "col"
                >{{ labels[col] }}</th>
            </tr>
        </thead>
        <tbody>
            <tr class = "table-row"
                v-for = "row in quotes"
            >
                <td
                    class="table-column_item"
                    v-for="column in cols"
                    :key="column"
                >
                    {{ row[column] }}
                </td>
            </tr>
        </tbody>
    </table>
</template>

<script setup>
import { getSession } from '@/session/sessions';
import { getCurrentInstance, nextTick, ref } from 'vue';

const loaded = ref(false);

const props = defineProps({
    quotes: {
        type: Array,
        required: false
    }
});

const cols = [
    "gallonsRequested", "deliveryAddress", "deliveryDate", "suggestedPriceperGallon", "totalAmountdue"
]

const quotes = [
    // {
    //     client: 'company1',
    //     gallonsRequested: 1000,
    //     deliveryAddress: 'Texas',
    //     deliveryDate: 'December',
    //     suggestedPriceperGallon: 50,
    //     totalAmountdue: 5000
    // },
    // {
    //     client: 'company2',
    //     gallonsRequested: 1500,
    //     deliveryAddress: 'California',
    //     deliveryDate: 'January',
    //     suggestedPriceperGallon: 50,
    //     totalAmountdue: 7500
    // },
    // {
    //     client: 'company3',
    //     gallonsRequested: 2000,
    //     deliveryAddress: 'New York',
    //     deliveryDate: 'February',
    //     suggestedPriceperGallon: 50,
    //     totalAmountdue: 10000
    // }
];

const labels = {
    client: 'Client',
    gallonsRequested: "Gallons",
    deliveryAddress: 'Delivery State',
    deliveryDate: 'Delivery Date',
    suggestedPriceperGallon: "Suggested Price",
    totalAmountdue: "Total Quoted"
}

// async function fetchHistory() {
//     // const url = 'http://127.0.0.1:8000/api/quote/history?session='  + getSession();
//     // const resp = await fetch(url);

//     // if (!resp.ok) {
//     //     throw Error("Failed to fetch quote history");
//     // }

//     // const data = await resp.json();
// }

setTimeout(() => {
    const url = 'http://127.0.0.1:8000/api/quote/history?session='  + getSession();
    fetch(url).then(response => {
        if(!response.ok) {
            throw Error("Failed to fetch quote history from server")
        } else {
            response.json().then(data => nextTick(() => {
                console.log("payload:")
                console.log(data)
                if (data.history.length > 0) {
                    for (var row of data.history) {
                        const newQuote = {
                            client: row.owner_id,
                            gallonsRequested: row.gallons_requested,
                            deliveryAddress: row.delivery_address,
                            deliveryDate: row.delivery_date,
                            suggestedPriceperGallon: row.suggested_price_per_gallon,
                            totalAmountdue: row.total_amount_due
                        };
                        quotes.push(newQuote);                        
                    }
                    console.log(quotes)
                    loaded.value = true
                    // const instance = getCurrentInstance();
                }
            }))
        }
    })
}, 0);

// if (Object.keys(routeData).length > 0) {
//     const newQuote = {
//         client: routeData.address,
//         gallonsRequested: routeData.gallons,
//         deliveryAddress: routeData.address,
//         deliveryDate: routeData.delivery,
//         suggestedPriceperGallon: routeData.price,
//         totalAmountdue: routeData.amount
//     };
//     quotes.push(newQuote);
//}

</script>

<style scoped>
.QuoteHeader {
    font-family: Avenir, Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: white;
    margin-top: 60px;
    margin-bottom: 10px;
}
.table-row {
    background: white;
}
.table-column_item {
    color: black;
    border: solid 1px #4d4d4d;
    padding: 8px 16px;
    box-sizing: border-box;
}

.table-header_item {
    background-color: lightgray;
}
</style>