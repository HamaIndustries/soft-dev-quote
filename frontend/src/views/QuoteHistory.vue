<template>
    <h1 class="QuoteHeader">Quote History</h1>
    <table>
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
                :key = "row.client"
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

const props = defineProps({
    quotes: {
        type: Array,
        required: false
    }
});

const cols = [
    "client", "gallonsRequested", "deliveryAddress", "deliveryDate", "suggestedPriceperGallon", "totalAmountdue"
]

const quotes = [
    {
        client: 'company1',
        gallonsRequested: 1000,
        deliveryAddress: 'Texas',
        deliveryDate: 'December',
        suggestedPriceperGallon: 50,
        totalAmountdue: 5000
    },
    {
        client: 'company2',
        gallonsRequested: 1500,
        deliveryAddress: 'California',
        deliveryDate: 'January',
        suggestedPriceperGallon: 50,
        totalAmountdue: 7500
    },
    {
        client: 'company3',
        gallonsRequested: 2000,
        deliveryAddress: 'New York',
        deliveryDate: 'February',
        suggestedPriceperGallon: 50,
        totalAmountdue: 10000
    }
];

const labels = {
    client: 'Client',
    gallonsRequested: "Gallons",
    deliveryAddress: 'Delivery State',
    deliveryDate: 'Delivery Date',
    suggestedPriceperGallon: "Suggested Price",
    totalAmountdue: "Total Quoted"
}
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