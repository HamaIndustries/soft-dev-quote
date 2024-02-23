<template>
    <h1>Quote History</h1>
    <div 
        class="table-row"
        v-for="row in quotes"
    >
        <div
            class="table-column_item"
            v-for="column in Object.keys(row)"
        >
            {{  row[column] }}
        </div>
    </div>
</template>


<script setup>

const quotes = [
    {
      client: 'company1',
      gallonsRequested: 1000,
      deliveryAddress: 'texas',
      deliveryDate: 'December',
      suggestedPriceperGallon: 50,
      totalAmountdue: 5000
    },
    
    {
      client: 'company2',
      gallonsRequested: 1000,
      deliveryAddress: 'texas',
      deliveryDate: 'December',
      suggestedPriceperGallon: 50,
      totalAmountdue: 5000
    },
    
    {
      client: 'company3',
      gallonsRequested: 1000,
      deliveryAddress: 'texas',
      deliveryDate: 'December',
      suggestedPriceperGallon: 50,
      totalAmountdue: 5000
    }
  ]


const props = defineProps({
    quotes: {
        type: Object,
        required: false
    }
})

props.quotes = quotes

</script>

<style scoped>
.table-row {
    display: flex;
    flex-wrap: nowrap;
}

.table-colum_item {
    width: 10%;
    border: solid 1px #4d4d4d;
    padding: 8px 16px;
    box-sizing: border-box;
}
</style>