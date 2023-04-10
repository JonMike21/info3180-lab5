<script setup>
import { ref, onMounted } from "vue";
import Card from "@/components/Card.vue";

let movies = ref([]);
let loading = ref(false);
let err = ref([]);
let test = ref('');



function fetchMovies(){
    loading.value=true;

    fetch("http://localhost:8080/api/v1/movies", {
        //method: 'GET',

    })
    .then((response) =>response.json())
    .then((data) => {
        movies.value = data.data;
        loading.value = false;
        test.value= 'http://localhost:8080/api/v1/posters/Asy.png'
        
    })
    .catch((error) => {
        console.log(error)
        loading.value = false;
        err.value = error.data
        // error.value = "Unable to fetch data";
    });
}

onMounted(() => {
    fetchMovies();
});

</script>

<template>
    <main class="container py-5">
        <h1 class="display-1 mb-3">movies</h1>
        <div v-if="loading" class="d-flex justify-content-center">
            <div class="spinner-border" style="width: 3rem; height: 3rem;" role="status">
                <span class="visually-hidden">Loading...</span>
            </div>
        </div>
        
    
        
        <ul v-if="!loading">
            <div v-if="err.length > 0" >{{ err }}</div>
            <div class="row row-cols-1 row-cols-md-4 g-4">
                <!--<img v-bind:src="test" class="card-img-top">-->
                <Card :movie="movie" v-for="movie in movies" :key="movie.id" />
            </div>
        </ul> 
    </main>
</template>