import os

# read two files which include list of images and videos and print them to slides

domain = 'https://something.here/'

html="""

<!doctype html>
<html lang="en">

	<head>
		<meta charset="utf-8">

		<title>reveal.js - Slide Backgrounds</title>

		<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">

		<link rel="stylesheet" href="%(domain)s/dist/reveal.css">
		<link rel="stylesheet" href="%(domain)s/dist/theme/serif.css" id="theme">
		<style type="text/css" media="screen">
			.slides section.has-dark-background,
			.slides section.has-dark-background h2 {
				color: #fff;
			}
			.slides section.has-light-background,
			.slides section.has-light-background h2 {
				color: #222;
			}
		</style>
	</head>
	<body>

		<div class="reveal">

			<div class="slides">
            %(slides)s
			</div>
		</div>
		<script src="https://wihnmqzi4wjykibxu3znzh0.z6.web.core.windows.net/dist/reveal.js"></script>
		<script>
			// Full list of configuration options:
			// https://revealjs.revealjs.com/config/
			Reveal.initialize({
				center: true,
				transition: 'linear',
				// transitionSpeed: 'slow',
				// backgroundTransition: 'slide'
			});
		</script>
	</body>
</html>
"""

img_slide = """
<section data-background-transition="slide" data-background="%(url)s">
<h2>%(name)s</h2>
</section>

"""

video_slide = """
<section data-background-video="%(url)s">
<h2>%(name)s</h2>
</section>

"""

slides = []

def main():
    with open('images.txt','r') as f:
        for line in f.read().splitlines():
            slides.append(img_slide % ({'name': os.path.basename(line), 'url': line}))
    with open('videos.txt','r') as f:
        for line in f.read().splitlines():
            slides.append(video_slide % ({'name': os.path.basename(line), 'url': line}))

    print (html % ({'slides': '\n'.join(slides), 'domain': domain}))

if __name__ == '__main__':
    main ()
