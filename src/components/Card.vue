<script setup>
const props = defineProps(['movie'])
</script>

<template>
    <div class="col col-md-4">
        <div class="card">
            <!--<img v-bind:src="movie.poster" class="card-img-top"> -->
            <img v-bind:src="'http://localhost:8080'+ movie.poster" class="card-img-top">
            <div class="card-body">
                <!--<h5 class="card-title">{{ movie.poster }}</h5>-->
                <h5 class="card-title">{{ movie.title }}</h5>
                <h6 class="card-subtitle mb-2 text-body-secondary">{{ movie.description }}</h6>
                <!-- <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.
                <RouterLink :to="'/movies/' + movie.id" class="card-link">Read more</RouterLink></p> -->
            </div>
        </div>
    </div>
</template>

<style>
    img{
        height: 300px; 
    }
</style>