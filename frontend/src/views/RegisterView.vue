<template>
    <div class="regisPage">
        <form class="regisForm" @submit.prevent="handleSubmit"> 
            <h1 class="regisHeader">Registration</h1>

            <label>Company Name: </label>
            <input type="text" required v-model="companyName">


            <label>Create Username: </label>
            <input type="text" required v-model="username">

            <label>Create Password: </label>
            <input type="password" required v-model="password">
            <div v-if="passwordError" class="pwError">{{ passwordError }}</div>

            <label>Confirm Password: </label>
            <input type="password" required v-model="confirmPassword">

            <SubmitButton type="submit">Create Account</SubmitButton>
        </form>

    </div>
</template>

<script scoped>

import SubmitButton from '@/components/SubmitButton.vue';

export default {
    data() {
        return {
            companyName: "",
            username: "",
            password: "",
            confirmPassword: "",
            passwordError: ""
        };
    },
    methods: {
        handleSubmit() {
            if (this.password.length < 5) {
                this.passwordError = "Password must be at least 5 characters long";
                return;
            }
            if (this.password !== this.confirmPassword) {
                this.passwordError = "Passwords do not match!";
                return;
            }
            this.passwordError = "";
            console.log("regis form submitted");
        }
    },
    components: { SubmitButton }
}


</script>

<style>

.body {
    color: #333;
    background-color: #eef2f3;
}

.regisPage {
    text-align: center;
    align-items: center;
}

.pwError {
    color: black;
    margin-top: 10px;
    font-size: bold;
    font-weight:400;
}

.regisHeader {
    font-family: Avenir, Arial, Helvetica, sans-serif;
    font-size: bold;
    margin-bottom: 20px;
    font-weight: 550;
    font-size: 40px;
    color: black;
    letter-spacing: 3px;
}
.regisForm {
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

