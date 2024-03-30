import Dr

<template>
    <div class="profilePage">
        <form class="profileForm" @submit.prevent="handleSubmit"> 
            <h1 class="profileHeader">Profile</h1>

            <label>Full Name: </label>
            <input type="text" required v-model="name">

            <label>Address 1: </label>
            <input type="text" required v-model="address1">
            
            <label>Address 2 (Optional): </label>
            <input type="text" v-model="address2">
            
            <div class="location">
                <label>City: </label>
                <input type="text" required v-model="city">

                <label>State: </label>
                <input type="dropdown" required v-model="state">
              
            </div>
           


        </form>

    </div>
</template>

<script>
export default {
    data() {
        return {
            name: "",
            address1: "",
            address2: ""
        };
    }
}
   
</script>

<style>

.profileHeader {
    font-family: Avenir, Arial, Helvetica, sans-serif;
    font-size: bold;
    margin-bottom: 20px;
    font-weight: 550;
    font-size: 40px;
    color: black;
    letter-spacing: 3px;
}
.profileForm {
    width: 600px;
    text-align: left;
    margin-left: 30px;
    background: white;
    padding:40px;
    border-radius: 15px;
}


label {
    color: #aaa;
    display: inline-block;
    margin: 25px 0 15px;
    text-transform: uppercase;
    letter-spacing: 2px;
    font-weight: bold;
}

input {
    display: block;
    padding: 10px 6px;
    width: 100%;
    box-sizing: border-box;
    border: none;
    border-bottom: 1px solid #ddd;
    color: rgb(68, 38, 38);
}

</style>
