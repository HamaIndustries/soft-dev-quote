<script setup>
</script>

<template>
    <button class="SubmitButton" @click="$emit('button-click')">
    <slot></slot>
    </button>
</template>

<style scoped>
    .SubmitButton {
        border: 0;
        padding: 10px 15px;
        font-family: Avenir, Arial, Helvetica, sans-serif;
        background:firebrick;
        color: white;
        border-radius: 20px;
        font-weight: 520;
        font-size: 25px;
        transition: 0.3s;
        letter-spacing: 1px;
    }

    .SubmitButton:hover {
      background: darkred;
    }
</style>