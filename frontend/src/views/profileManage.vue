

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
               
            <div style="display:flex; flex-flow: row nowrap; align-items: baseline;">
                <SubmitButton type="submit" class="save">Save Information</SubmitButton>
                <div v-if="success" style="color:green;margin-left:auto;">Information updated successfully</div>
            </div>

        </form>

    </div>
</template>

<script>

import SubmitButton from '@/components/SubmitButton.vue';
import { getSession } from '@/session/sessions';

export default {
    data() {
        return {
            profile: {},
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
        success: false
        }
    },

    created() {
        this.fetchProfile();
    },

    methods: {
        async fetchProfile() {
        try {
            const response = await fetch('http://127.0.0.1:8000/api/profile_mgmt?session=' + getSession());
            if (!response.ok) {
            throw new Error('Network response was not ok');
            }
            const data = await response.json();
            
            this.profile = data;
            this.setVals(data);
        } catch (error) {
            console.error('There was a problem with the fetch operation:', error);
        }
    },

    setVals(data) {
        for (var key of Object.keys(data)) {
            this[key] = data[key]
        }
    },

    async postData() {
    try {
      const response = await fetch('http://127.0.0.1:8000/api/profile_mgmt?session=' + getSession(), {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({ 
          name: this.name,
          address1: this.address1,
          address2: this.address2,
          city: this.city,
          state: this.state,
          zipcode: this.zipcode
        })
      });
      if (!response.ok) {
        this.success = false
        throw new Error('Network response was not ok');
      }
      const data = await response.json(); // get json data from backend
      this.success = true;
      console.log('Data received:', data); // display it

    } catch (error) {
        this.success = false
      console.error('There was a problem with the fetch operation:', error);
        }
    },


    handleSubmit() {
        const zipSr = String(this.zipcode);
        if (zipSr.length < 5 || zipSr.length > 9) {
            this.zipcodeError = "Zipcode must be 5 to 9 characters long!";
            return;
        }

        this.zipcodeError = "";
        console.log("profile form updated");

        this.postData(); // send frontend data to backend on submit
    }
},


    components: {
    SubmitButton,
    SubmitButton
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
    margin-top: 2rem;
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
