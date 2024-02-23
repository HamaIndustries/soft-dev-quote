

<template>
    <div class="profilePage">
        <form class="profileForm" @submit.prevent="handleSubmit"> 
            <h1 class="profileHeader">Profile</h1>

            <div v-if="zipcodeError" class="zcError">{{ zipcodeError }}</div>

            <label>Full Name: </label>
            <input type="text" required v-model="name">

            <label>Address 1: </label>
            <input type="text" required v-model="address1">
            
            <label>Address 2 (Optional): </label>
            <input type="text" v-model="address2">
            
          
                <label>City: </label>
                <input type="text" required v-model="city">
                
            <div class="location">
                <label>State:</label>
                <select class="dropdown" v-model="state" required>
                    <option v-for="state in states" :key="state" :value="state">{{ state }}</option>
                </select>

                <label>Zip Code: </label>
                <input class="zip" type="number" required v-model="zipcode">
            </div>
               
            <button type="submit" class="save">Save Information</button>

        </form>

    </div>
</template>

<script>

export default {
    data() {
        return {
            name: "",
            address1: "",
            address2: "",
            city: "",
            state: "",
            zipcode: "",
            zipcodeError: "",
            favorites: [], 
            states: [
          'Alabama', 'Alaska', 'American Samoa', 'Arizona',
          'Arkansas', 'California', 'Colorado', 'Connecticut',
          'Delaware', 'District of Columbia', 'Federated States of Micronesia',
          'Florida', 'Georgia', 'Guam', 'Hawaii', 'Idaho',
          'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky',
          'Louisiana', 'Maine', 'Marshall Islands', 'Maryland',
          'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi',
          'Missouri', 'Montana', 'Nebraska', 'Nevada',
          'New Hampshire', 'New Jersey', 'New Mexico', 'New York',
          'North Carolina', 'North Dakota', 'Northern Mariana Islands', 'Ohio',
          'Oklahoma', 'Oregon', 'Palau', 'Pennsylvania', 'Puerto Rico',
          'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee',
          'Texas', 'Utah', 'Vermont', 'Virgin Island', 'Virginia',
          'Washington', 'West Virginia', 'Wisconsin', 'Wyoming',
        ],
            
        };
    },

    methods: {
        handleSubmit() {
            const zipSr = String(this.zipcode);
            if (zipSr.length < 5) {
                this.zipcodeError = "Zipcode must be at least 5 characters long!";
                return;
            }
    
            this.zipcodeError = "";
            console.log("profile form updated")
        }
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

.location {
    display: flex;
    justify-content: space-between;
}

.dropdown {
    margin-top: 20px;
    margin-right:10px;
    border:0;
    transition: 0.3s;
}

.dropdown:hover {
    background: lightgray;
}

.zip {
    width:100px;
    margin-top:20px;
}

.zcError {
    color: black;
}
.save {
    border: 0;
    padding: 10px 15px;
    font-family: Avenir, Arial, Helvetica, sans-serif;
    margin-top: 80px;
    background:lightskyblue;
    color: white;
    border-radius: 20px;
    font-weight: 520;
    font-size:25px;
    transition: 0.3s;
    letter-spacing: 1px;
}

.save:hover {
    background: darkcyan;
}

select {
    text-align: center;
    margin-left:10px;
    border-radius:10px;
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
