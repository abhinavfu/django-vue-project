<template>
    <nav>
        <div class="logo">
            <img src="https://www.themoviedb.org/assets/2/v4/logos/v2/blue_short-8e7b30f73a4020692ccca9c88bafe5dcb6f8a62a4c6bc55cd9ba82bb2cd95f6c.svg" alt="">
            <ul>
                <li>Movies</li>
                <li>TV Shows</li>
                <li>People</li>
                <li>More</li>
            </ul>
        </div>
        <ul>
            <li>Overview</li>
            <li>Media</li>
            <li>Fandom</li>
            <li>Share</li>
        </ul>
    </nav>
    <!-- <div class="uni-padding movie-container" :style="{ backgroundImage: `url(${photo})` }"> -->
    <div class="uni-padding movie-container">
        <div class="img-container">
            <img :src="photo" alt="">
            <div class="watch-now">
                <div class="logo-watch">
                    Hotstar
                </div>
                <div>
                    <h3 class="text-gray">Now Streaming</h3>
                    <h3>Watch Now</h3>
                </div>
            </div>
        </div>
        <div class="info-container">
            <h1 class="movie-title">{{movie.Title}} <span>({{ movie.Year }})</span></h1>
            <div class="movie-details">
                <span class="rated">{{movie.Rated}}</span>
                <span>{{movie.Released}}</span>
                <span>{{movie.Genre}}</span>
                <span>{{movie.Runtime}}</span>
            </div>
            <div class="movie-ratings">
                <div v-for="item in movie.Ratings" :key="item">
                    <MovieRating :values="item.Value" :source="item.Source"/>
                </div>
            </div>
            <div class="btns-container">
                <span class="btn"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512"><path d="M40 48C26.7 48 16 58.7 16 72l0 48c0 13.3 10.7 24 24 24l48 0c13.3 0 24-10.7 24-24l0-48c0-13.3-10.7-24-24-24L40 48zM192 64c-17.7 0-32 14.3-32 32s14.3 32 32 32l288 0c17.7 0 32-14.3 32-32s-14.3-32-32-32L192 64zm0 160c-17.7 0-32 14.3-32 32s14.3 32 32 32l288 0c17.7 0 32-14.3 32-32s-14.3-32-32-32l-288 0zm0 160c-17.7 0-32 14.3-32 32s14.3 32 32 32l288 0c17.7 0 32-14.3 32-32s-14.3-32-32-32l-288 0zM16 232l0 48c0 13.3 10.7 24 24 24l48 0c13.3 0 24-10.7 24-24l0-48c0-13.3-10.7-24-24-24l-48 0c-13.3 0-24 10.7-24 24zM40 368c-13.3 0-24 10.7-24 24l0 48c0 13.3 10.7 24 24 24l48 0c13.3 0 24-10.7 24-24l0-48c0-13.3-10.7-24-24-24l-48 0z"/></svg></span>
                <span class="btn"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512"><path d="M47.6 300.4L228.3 469.1c7.5 7 17.4 10.9 27.7 10.9s20.2-3.9 27.7-10.9L464.4 300.4c30.4-28.3 47.6-68 47.6-109.5v-5.8c0-69.9-50.5-129.5-119.4-141C347 36.5 300.6 51.4 268 84L256 96 244 84c-32.6-32.6-79-47.5-124.6-39.9C50.5 55.6 0 115.2 0 185.1v5.8c0 41.5 17.2 81.2 47.6 109.5z"/></svg></span>
                <span class="btn"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 384 512"><path d="M0 48V487.7C0 501.1 10.9 512 24.3 512c5 0 9.9-1.5 14-4.4L192 400 345.7 507.6c4.1 2.9 9 4.4 14 4.4c13.4 0 24.3-10.9 24.3-24.3V48c0-26.5-21.5-48-48-48H48C21.5 0 0 21.5 0 48z"/></svg></span>
                <span class="btn-play"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 384 512"><path d="M73 39c-14.8-9.1-33.4-9.4-48.5-.9S0 62.6 0 80L0 432c0 17.4 9.4 33.4 24.5 41.9s33.7 8.1 48.5-.9L361 297c14.3-8.7 23-24.2 23-41s-8.7-32.2-23-41L73 39z"/></svg> Play Trailer</span>
            </div>
            <div class="movie-overview">
                <div>Obviously.</div>
                <h3>Overview</h3>
                <div>{{ movie.Plot }}</div>
                <br>
                <ul>
                    <li>
                        <h3>{{ movie.Director }}</h3>
                        <p>Director</p>
                    </li>
                    <li>
                        <h3>{{ movie.Actors }}</h3>
                        <p>Actors</p>
                    </li>
                    <li>
                        <h3>{{ movie.Writer }}</h3>
                        <p>Writers</p>
                    </li>
                </ul>
            </div>
        </div>
    </div>
    <div class="uni-padding movie-other-details">
        <ul>
            <li>
                <h3>Language</h3>
                <p>{{ movie.Language }}</p>
            </li>
            <li>
                <h3>Country</h3>
                <p>{{ movie.Country }}</p>
            </li>
            <li>
                <h3>BoxOffice</h3>
                <p>{{ movie.BoxOffice }}</p>
            </li>
            <li>
                <h3>Type</h3>
                <p>{{ movie.Type }}</p>
            </li>
            <li>
                <h3>DVD</h3>
                <p>{{ movie.DVD }}</p>
            </li>
            <li>
                <h3>Production</h3>
                <p>{{ movie.Production }}</p>
            </li>
            <li>
                <h3>Website</h3>
                <p>{{ movie.Website }}</p>
            </li>
        </ul>
        <div class="ratings">
            <h2>Ratings</h2>
            <ul>
                <li>
                    <h3>Metascore</h3>
                    <p>{{ movie.Metascore }}</p>
                </li>
                <li>
                    <h3>imdbRating</h3>
                    <p>{{ movie.imdbRating }}</p>
                </li>
                <li>
                    <h3>imdbVotes</h3>
                    <p>{{ movie.imdbVotes }}</p>
                </li>
                <li>
                    <h3>imdbID</h3>
                    <p>{{ movie.imdbID }}</p>
                </li>
            </ul>
        </div>
        <div>
            <h2>Awards</h2>
            <p>{{ movie.Awards }}</p>
        </div>
    </div>

</template>

<script>
import axios from 'axios';
import MovieRating from './Rating.vue';

export default {
    name: 'HomePage',
    components: {
        MovieRating,
    },
    data(){
        return {
            movie:[],
        }
    },
    async mounted(){
        let api_result = await axios.get("http://www.omdbapi.com/?i=tt3896198&apikey=d2132124")
        console.log(api_result.data)
        this.movie = api_result.data
    },
    computed: {
    photo() {
      return this.movie.Poster;
    }
  }
}
</script>

<style scoped>
img{
    width: 100%;
    height: auto;
}
svg{
    width: 16px;
    height: 16px;
}
nav .logo{
    background-color: rgb(0, 0, 76);
    padding: 0px 10%;
    color: white;
    display: flex;
    align-items: center;
    gap: 20px;
}
nav .logo img{
    height: 15px;
    width: auto;
}
nav ul{
    padding: 5px;
    display: flex;
    justify-content: center;
    gap: 20px;
}
.uni-padding{
    padding: 30px 10%;
}
.movie-container{
    display: flex;
    background-repeat: no-repeat;
    background-size: cover;
    background-position: center;
    background-color: rgba(0, 0, 0, 0.2);
    gap: 40px;
    justify-content: center;
    color: white;
    background-color: rgba(10, 10, 40, 0.8);
    overflow: hidden;
}
.img-container{
    width: 400px;
    border-radius: 10px;
    overflow: hidden;
    background-color: rgb(61, 60, 60);
}
.img-container .watch-now{
    width: 100%;
    display: flex;
    gap: 10px;
    justify-content: center;
    padding: 10px;
    cursor: pointer;
}
.watch-now .logo-watch{
    height: 35px;
    width: auto;
    padding: 5px;
    border-radius: 4px;
    font-size: 12px;
    font-weight: 500;
    background-color: white;
    color: rgb(27, 26, 26);
    display: flex;
    justify-content: center;
    align-items: center;
}
.watch-now div h3{
    margin: 0px;
    color: white;
}
.watch-now div .text-gray{
    color: rgb(170, 170, 170);
}
.info-container{
    width: 100%;
}
.info-container .movie-title span{
    font-weight: 400;
    color: gray;
}
.info-container .movie-details{
    display: flex;
    align-items: center;
    gap: 10px;
}
.info-container .movie-details .rated{
    border: 1px solid gray;
    color: gray;
    padding: 2px 4px;
    border-radius: 4px;
}
.info-container .movie-ratings {
    display: flex;
    align-items: center;
    gap: 20px;
    margin: 20px 0px;
}
.info-container .btns-container{
    margin: 20px 0px;
    display: flex;
    gap: 20px;
    margin: 20px 0px;
    align-items: center;
}
.info-container .btns-container .btn{
    width: 45px;
    height: 45px;
    border-radius: 25px;
    background-color: rgb(61, 60, 60);
    display: flex;
    justify-content: center;
    align-items: center;
    cursor: pointer;
}
.info-container .btns-container .btn-play{
    cursor: pointer;
    font-weight: 500;
}
.info-container .btns-container .btn-play:hover{
    color: rgb(173, 173, 173);
}
.info-container .btns-container svg{
    fill: white;
}
.movie-overview > h3{
    margin: 10px 0px;
}
ul{
    list-style: none;
}
ul li{
    padding: 5px;
    margin: 5px 0px;
}
.movie-other-details ul{
    display: flex;
    flex-wrap: wrap;
    gap: 20px;
    /* justify-content: space-evenly; */
}
.ratings{
    margin: 40px 0px;
}

/* ------------ Mobile devices ------------ */
@media only screen and (max-width: 900px) {
.movie-container{
    display: block;
    
}
.img-container{
    /* max-height: 420px; */
    margin-bottom: 20px;
}
}
@media only screen and (max-width: 450px) {
.movie-container{
    display: flex;
    flex-wrap: wrap;
    
}

}
</style>