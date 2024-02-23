<template>
    <h1 class="QuoteHeader">Quote History</h1>
    <div 
        class="table-row"
        v-for="row in quotes"
        :key="row.client"
    >
        <div
            class="table-column_item"
            v-for="column in Object.keys(row)"
            :key="column"
        >
            {{ row[column] }}
        </div>
    </div>
</template>

<script setup>
import { defineProps } from 'vue';

const props = defineProps({
    quotes: {
        type: Array,
        required: false
    }
});

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
    display: flex;
    flex-wrap: nowrap;
    background: white;
}
.table-column_item {
    color: black;
    width: 20%;
    border: solid 1px #4d4d4d;
    padding: 8px 16px;
    box-sizing: border-box;
}
</style>