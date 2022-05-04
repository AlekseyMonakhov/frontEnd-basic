const gulp = require('gulp');
const sass = require('gulp-sass')(require('sass'));
const server = require('browser-sync').create();

gulp.task("css", () => {
    return gulp
        .src('./src/styles/style.scss')
        .pipe(sass())
        .pipe(gulp.dest('dist'))
        .pipe(server.stream());
});

gulp.task("html", () => {
    return gulp
        .src('./src/index.html')
        .pipe(gulp.dest('dist'))
        .pipe(server.stream());
});

gulp.task("images", () => {
    return gulp
        .src('./src/images/*')
        .pipe(gulp.dest('dist/images'));
});

gulp.watch("./src/styles/**/*.scss", gulp.task("css"))
gulp.watch("./src/index.html", gulp.task("html"))

gulp.task('serve', function() {
    server.init({
        server: {
            baseDir: "dist"
        },
        notify: true
    });
});


gulp.task("start", gulp.series("images", "css", "html", "serve"));