Flagtastic
An SVG framework

I wanted a framework similar to fontawesome but for flags. The flags used in this framework were downloaded from flaticon.com (see license folder). There flags are great for displaying languages, user's location and more!
All the SVGs, the css and functionality are packed into a js file. You no longer need a folder with 250 odd images.

To get started, include the file into the head of your document:
<script src="vendor/flagtastic.min.js">

Including a flag is easy:
<i class="fl fl-de"></i>
This includes a German flag. Flags are denoted using ISO2 codes.

Here are some other flags:
<i class="fl fl-us"></i>
<i class="fl fl-mx"></i>
<i class="fl fl-ca"></i>

You can also control your flags sizes using the following classes:
<i class="fl fg-us fl-xs"></i>
<i class="fl fg-us fl-sm"></i>
<i class="fl fg-us fl-md"></i> (Default size)
<i class="fl fg-us fl-lg"></i>
<i class="fl fg-us fl-xl"></i>

I hope you find it useful!

Adding flags at runtime is easy but you need to call the updateFlags() function to make them display:
function addSpanishFlag() {
  // Create the new flag and append it
  let flag = document.createElement('i');
  flag.className = 'fl fl-es';
  document.body.appendChild(flag);
  // Update the flags
  updateFlags();
}