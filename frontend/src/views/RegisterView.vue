<template>
    <div class="regisPage">
        <h1 class="regisHeader">Registration</h1>
        <form class="regisForm"> 
            <label>Create Username: </label>
            <input type="text" required v-model="username">

            <label>Create Password: </label>
            <input type="password" required v-model="password">

            <label>Confirm Password: </label>
            <input type="password" required v-model="confirmPassword">

            <button type="submit" class="createAccount">Create Account</button>
        </form>

    </div>
</template>

<script>
export default {
    data() {
        return {
            username: "",
            password: ""
        };
    }
}


</script>

<style>

.body {
    color: #333;
    background-color: #eef2f3;
}

.regisPage {
    text-align: center;
}

.regisHeader {
    padding-left: 30px;
    font-size: bold;
    margin-bottom: 20px;
    font-weight: 550;
    font-size: 40px;
    color: white;
    letter-spacing: 3px;
}
.regisForm {
    width: 600px;
    text-align: left;
    margin-left: 30px;
    background: white;
    padding:40px;
    border-radius: 10px;
}

.createAccount {
    margin-top: 35px;
    margin-left: 120px;
    background:lightskyblue;
    color: white;
    border-radius: 10px;
    font-weight: 520;
    font-size:30px;
    transition: 0.3s;
    letter-spacing: 1px;

}
.createAccount:hover {
    background: darkcyan;
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

