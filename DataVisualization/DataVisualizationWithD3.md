# Data Visualization with D3 

Data Visualization with D3 projects are from [freeCodeCamp](https://www.freecodecamp.org/learn/data-visualization/)

## Add Document Elements with D3

**The Lesson:**

D3 has several methods that let you add and change elements in your document.

The `select()` method selects one element from the document. It takes an argument for the name of the element you want and returns an HTML node for the first element in the document that matches the name. 

**Example:**

Here's an example:

```Javascript
const anchor = d3.select("a");
```

The above example finds the first anchor tag on the page and saves an HTML node for it in the variable anchor. You can use the selection with other methods. The d3 part of the example is a reference to the D3 object, which is how you access D3 methods.

Two other useful methods are `append()` and `text()`.

The `append()` method takes an argument for the element you want to add to the document. It appends an HTML node to a selected item, and returns a handle to that node.

The `text()` method either sets the text of the selected node, or gets the current text. To set the value, you pass a string as an argument inside the parentheses of the method.

**Example:**

Here's an example that selects an unordered list, appends a list item, and adds text:

```Javascript 
d3.select("ul")
  .append("li")
  .text("Very important item");
D3 allows you to chain several methods together with periods to perform a number of actions in a row.
```


**Challange Instructions:**
Use the select method to select the `body` tag in the document. Then append an `h1` tag to it, and add the text "Learning D3" into the `h1` element.


**My Solution**
```JavaScript
<body>
  <script>
    // Add your code below this line
    d3.select("body")
      .append("h1")
      .text("Learning D3");    
    // Add your code above this line
  </script>
</body>
```

## Select a Group of Elements with D3

**The Lesson:**

D3 also has the selectAll() method to select a group of elements. It returns an array of HTML nodes for all the items in the document that match the input string. 


**Example:**

Here's an example to select all the anchor tags in a document:

```Javascript

const anchors = d3.selectAll("a");

```
Like the `select()` method, `selectAll()` supports method chaining, and you can use it with other methods.

**Challenge Instructions:**

Select all of the li tags in the document, and change their text to the string list item by chaining the `.text()` method.

**My Solution:**

```Javascript 
<body>
  <ul>
    <li>Example</li>
    <li>Example</li>
    <li>Example</li>
  </ul>
  <script>
    // Add your code below this line

const achors = d3.selectAll("li")
  .text("list item");

    // Add your code above this line
  </script>
</body>

```

## Work with Data in D3

**The Lesson:**

The D3 library focuses on a data-driven approach. When you have a set of data, you can apply D3 methods to display it on the page. Data comes in many formats, but this challenge uses a simple array of numbers.

The first step is to make D3 aware of the data. The `data()` method is used on a selection of DOM elements to attach the data to those elements. The data set is passed as an argument to the method.

A common workflow pattern is to create a new element in the document for each piece of data in the set. D3 has the `enter()` method for this purpose.

When `enter()` is combined with the data() method, it looks at the selected elements from the page and compares them to the number of data items in the set. If there are fewer elements than data items, it creates the missing elements.


**Example:**

Here is an example that selects a `ul` element and creates a new list item based on the number of entries in the array:

```Javascript 
<body>
  <ul></ul>
  <script>
    const dataset = ["a", "b", "c"];
    d3.select("ul").selectAll("li")
      .data(dataset)
      .enter()
      .append("li")
      .text("New item");
  </script>
</body>
```


It may seem confusing to select elements that don't exist yet. This code is telling D3 to first select the `ul` on the page. Next, select all list items, which returns an empty selection. Then the `data()` method reviews the dataset and runs the following code three times, once for each item in the array. The enter() method sees there are no `li` elements on the page, but it needs 3 (one for each piece of data in dataset). New `li` elements are appended to the `ul` and have the text New item.

It may seem confusing to select elements that don't exist yet. This code is telling D3 to first select the `ul` on the page. Next, select all list items, which returns an empty selection. Then the `data()` method reviews the dataset and runs the following code three times, once for each item in the array. The enter() method sees there are no `li`
 elements on the page, but it needs 3 (one for each piece of data in `dataset`). New `li` elements are appended to the ul and have the text New item.



**Challenge Instructions:**

Select the body node, then select all `h2` elements. Have D3 create and append an `h2` tag for each item in the dataset array. The text in the `h2` should say `New Title`. Your code should use the `data()` and `enter()` methods.

**My Solution:**
```Javascript
<body>
  <script>
    const dataset = [12, 31, 22, 17, 25, 18, 29, 14, 9];

    // Add your code below this line

   d3.select("body").selectAll("h2")
      .data(dataset)
      .enter()
      .append("h2")
      .text("New Title");

    // Add your code above this line
  </script>
</body>
```

## Work with Dynamic Data in D3

**The Lesson:**

The last two challenges cover the basics of displaying data dynamically with D3 using the `data()` and `enter()` methods. These methods take a data set and, together with the `append()` method, create a new DOM element for each entry in the data set.

In the previous challenge, you created a new `h2` element for each item in the `dataset` array, but they all contained the same text, `New Title`. This is because you have not made use of the data that is bound to each of the `h2` elements.

The D3 `text()` method can take a string or a callback function as an argument:
```Javascript
selection.text((d) => d)
```


In the example above, the parameter d refers to a single entry in the dataset that a selection is bound to.

Using the current example as context, the first `h2`  element is bound to 12, the second `h2`  element is bound to 31, the third `h2`  element is bound to 22, and so on.



**Challenge Instructions:**

Change the `text()` method so that each `h2` element displays the corresponding value from the `dataset` array with a single space and the string `USD`. For example, the first heading should be `12 USD`.

**My Solution:**

```Javascript 
  <body>
  <script>
    const dataset = [12, 31, 22, 17, 25, 18, 29, 14, 9];

    d3.select("body").selectAll("h2")
      .data(dataset)
      .enter()
      .append("h2")
      // Add your code below this line

      .text((d) => d + " " + "USD");

      // Add your code above this line
  </script>
</body>

```


## Add Inline Styling to Elements

**The Lesson:**

D3 lets you add inline CSS styles on dynamic elements with the style() method.

The `style()` method takes a comma-separated key-value pair as an argument. Here's an example to set the selection's text color to blue:

**Example:**

```Javascript 
selection.style("color","blue");
```

**Challenge Instructions:**


Add the `style()` method to the code in the editor to make all the displayed text have a `font-family` of `verdana`.

**My Solution:**

```Javascript 

<body>
  <script>
    const dataset = [12, 31, 22, 17, 25, 18, 29, 14, 9];

    d3.select("body").selectAll("h2")
      .data(dataset)
      .enter()
      .append("h2")
      .text((d) => (d + " USD"))
      // Add your code below this line

.style("font-family", "verdana");

      // Add your code above this line
  </script>
</body>
```

## Change Styles Based on Data 

**The Lesson:**

D3 is about visualization and presentation of data. It's likely you'll want to change the styling of elements based on the data. For example, you may want to color a data point blue if it has a value less than 20, and red otherwise. You can use a callback function in the `style()` method and include the conditional logic. The callback function uses the d parameter to represent the data point:

**Example:**

```Javascript 
selection.style("color", (d) => { });
```

The `style()` method is not limited to setting the color - it can be used with other CSS properties as well.


**Challenge Instructions:**

Add the `style()` method to the code in the editor to set the `color` of the `h2` elements conditionally. Write the callback function so if the data value is less than 20, it returns red, otherwise it returns green.

Note: You can use if-else logic, or the ternary operator.

**My Solution first attempt:**

```Javascript 
<body>
  <script>
    const dataset = [12, 31, 22, 17, 25, 18, 29, 14, 9];

    d3.select("body").selectAll("h2")
      .data(dataset)
      .enter()
      .append("h2")
      .text((d) => (d + " USD"))
      // Add your code below this line
if h2 <20
.style("color", "red");
else 
.style("color","blue");

      // Add your code above this line
  </script>
</body>
```

**My Solution second attempt (the correct solution):**

```Javascript 
<body>
  <script>
    const dataset = [12, 31, 22, 17, 25, 18, 29, 14, 9];

    d3.select("body").selectAll("h2")
      .data(dataset)
      .enter()
      .append("h2")
      .text((d) => (d + " USD"))
      // Add your code below this line
      .style("color", d => d < 20 ? "red" : "green");  

      // Add your code above this line
  </script>
</body>

```

Resource: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Conditional_operator


## Add Classes with D3 

**The Lesson:**

Using a lot of inline styles on HTML elements gets hard to manage, even for smaller apps. It's easier to add a class to elements and style that class one time using CSS rules. D3 has the `attr()` method to add any HTML attribute to an element, including a class name.

The `attr()` method works the same way that `style()` does. It takes comma-separated values, and can use a callback function. Here's an example to add a class of `container` to a selection:



**Example:**

```Javascript 
selection.attr("class", "container");

```

Note that the `class` parameter will remain the same whenever you need to add a class and only the `container` parameter will change.
**Challenge Instructions:**



Add the attr() method to the code in the editor and put a class of bar on the div elements.

**My Solution:**

```Javascript 
<style>
  .bar {
    width: 25px;
    height: 100px;
    display: inline-block;
    background-color: blue;
  }
</style>
<body>
  <script>
    const dataset = [12, 31, 22, 17, 25, 18, 29, 14, 9];

    d3.select("body").selectAll("div")
      .data(dataset)
      .enter()
      .append("div")
      // Add your code below this line
      
    .attr("class", "bar")

      // Add your code above this line
  </script>
</body>

```
## Update the Height of an Element Dynamically

**The Lesson:**

The previous challenges covered how to display data from an array and how to add CSS classes. You can combine these lessons to create a simple bar chart. There are two steps to this:

1. Create a `div` for each data point in the array

1. Give each `div` a dynamic height, using a callback function in the `style()` method that sets height equal to the data value

Recall the format to set a style using a callback function:

**Example:**

```Javascript 
selection.style("cssProperty", (d) => d)
```

**Challenge Instructions:**

Add the `style()` method to the code in the editor to set the `height` property for each element. Use a callback function to return the value of the data point with the string `px` added to it.

**My Solution:**

```Javascript 
.style("height", (d) => d + 'px')

```


## Change the Presentation of a Bar Chart 

**The Lesson:**

The last challenge created a bar chart, but there are a couple of formatting changes that could improve it:

1. Add space between each `bar` to visually separate them, which is done by adding a margin to the CSS for the bar class

1. Increase the height of the bars to better show the difference in values, which is done by multiplying the value by a number to scale the height


**Example:**

```Javascript 
No example for this exercise
```

**Challenge Instructions:**

First, add a `margin` of `2px` to the bar class in the `style` tag. Next, change the callback function in the `style()` method so it returns a value `10` times the original data value (plus the `px`).

Note: Multiplying each data point by the same constant only alters the scale. It's like zooming in, and it doesn't change the meaning of the underlying data.

**My Solution:**

```Javascript 
<style>
  .bar {
    width: 25px;
    height: 100px;
    /* Add your code below this line */
    margin: 2px;

    
    /* Add your code above this line */
    display: inline-block;
    background-color: blue;
  }
</style>
<body>
  <script>
    const dataset = [12, 31, 22, 17, 25, 18, 29, 14, 9];

    d3.select("body").selectAll("div")
      .data(dataset)
      .enter()
      .append("div")
      .attr("class", "bar")
      .style("height", (d) => (d*10 + "px")) // Change this line
  </script>
</body>

```

## Learn About SVG in D3

**The Lesson:**

SVG stands for Scalable Vector Graphics.

Here "scalable" means that, if you zoom in or out on an object, it would not appear pixelated. It scales with the display system, whether it's on a small mobile screen or a large TV monitor.

SVG is used to make common geometric shapes. Since D3 maps data into a visual representation, it uses SVG to create the shapes for the visualization. SVG shapes for a web page must go within an HTML `svg` tag.

CSS can be scalable when styles use relative units (such as `vh`, `vw`, or percentages), but using SVG is more flexible to build data visualizations.

**Example:**

```Javascript 

```

**Challenge Instructions:**

Add an svg node to the body using `append()`. Give it a width attribute set to the provided w constant and a height attribute set to the provided `h` constant using the `attr()` or `style()` methods for each. You'll see it in the output because there's a `background-color` of pink applied to it in the style tag.

**Note:** When using `attr()` width and height attributes do not have units. This is the building block of scaling - the element will always have a 5:1 width to height ratio, no matter what the zoom level is.

**My Solution:**

```Javascript 

<style>
  svg {
    background-color: pink;
  }
</style>
<body>
  <script>
    const dataset = [12, 31, 22, 17, 25, 18, 29, 14, 9];

    const w = 500;
    const h = 100;

    const svg = d3.select("body")
                  // Add your code below this line
 .append("svg")
        .attr("width", w)
        .attr("height", h);  


                  // Add your code above this line
  </script>
</body>
```



## Display Shapes with SVG

**The Lesson:**

The last challenge created an svg element with a given width and height, which was visible because it had a background-color applied to it in the style tag. The code made space for the given width and height.

The next step is to create a shape to put in the svg area. There are a number of supported shapes in SVG, such as rectangles and circles. They are used to display data. For example, a rectangle (`<rect>`) SVG shape could create a bar in a bar chart.

When you place a shape into the svg area, you can specify where it goes with `x` and `y` coordinates. The origin point of (`0, 0`) is in the upper-left corner. Positive values for `x` push the shape to the right, and positive values for `y` push the shape down from the origin point.

To place a shape in the middle of the 500 (width) x 100 (height) `svg` from last challenge, the `x` coordinate would be `250` and the `y` coordinate would be `50`.

An SVG `rect` has four attributes. There are the `x` and `y` coordinates for where it is placed in the svg area. It also has a `height` and `width` to specify the size.

**Example:**

```Javascript 

```

**Challenge Instructions:**
  
Add a rect shape to the svg using `append()`, and give it a `width` attribute of 25 and `height` attribute of 100. Also, give the rect `x` and `y` attributes each set to `0`.

**My Solution:**

```Javascript 
<body>
  <script>
    const dataset = [12, 31, 22, 17, 25, 18, 29, 14, 9];

    const w = 500;
    const h = 100;

    const svg = d3.select("body")
                  .append("svg")
                  .attr("width", w)
                  .attr("height", h)
                  // Add your code below this line
                  .append("rect")
                  .attr("width", 25)
                  .attr("height", 100)
                  .attr("x", 0)
                  .attr("y",0);


                  // Add your code above this line
  </script>
</body>
```


## Create a Bar for Each Data Point in the Set

**The Lesson:**

The last challenge added only one rectangle to the `svg` element to represent a bar. Here, you'll combine what you've learned so far about `data()`, `enter()`, and SVG shapes to create and append a rectangle for each data point in `dataset`.

A previous challenge showed the format for how to create and append a `div` for each item in `dataset`:


**Example:**

```Javascript 

d3.select("body").selectAll("div")
  .data(dataset)
  .enter()
  .append("div")
  
```

There are a few differences working with `rect` elements instead of `div` elements. The `rect` elements must be appended to an `svg` element, not directly to the `body`. Also, you need to tell D3 where to place each `rect` within the `svg` area. The bar placement will be covered in the next challenge.

**Challenge Instructions:**

Use the `data()`, `enter()`, and `append()` methods to create and append a rect for each item in dataset. The bars should display all on top of each other; this will be fixed in the next challenge.

**My Solution:**

```Javascript 
<body>
  <script>
    const dataset = [12, 31, 22, 17, 25, 18, 29, 14, 9];

    const w = 500;
    const h = 100;

    const svg = d3.select("body")
                  .append("svg")
                  .attr("width", w)
                  .attr("height", h);

    svg.selectAll("rect")
       // Add your code below this line

d3.select("body").selectAll("div")
  .data(dataset)
  .enter()
  .append("rect")

       // Add your code above this line
       .attr("x", 0)
       .attr("y", 0)
       .attr("width", 25)
       .attr("height", 100);
  </script>
</body>

```

## Dynamically Set the Coordinates for Each Bar 

**The Lesson:**

The last challenge created and appended a rectangle to the `svg` element for each point in `dataset` to represent a bar. Unfortunately, they were all stacked on top of each other.

The placement of a rectangle is handled by the `x` and `y` attributes. They tell D3 where to start drawing the shape in the `svg` area. The last challenge set them each to 0, so every bar was placed in the upper-left corner.

For a bar chart, all of the bars should sit on the same vertical level, which means the `y` value stays the same (at 0) for all bars. The `x` value, however, needs to change as you add new bars. Remember that larger `x` values push items farther to the right. As you go through the array elements in `dataset`, the `x` value should increase.

The `attr()` method in D3 accepts a callback function to dynamically set that attribute. The callback function takes two arguments, one for the data point itself (usually `d`) and one for the index of the data point in the array. The second argument for the index is optional. Here's the format:



**Example:**

```Javascript 
selection.attr("property", (d, i) => { })


```

It's important to note that you do NOT need to write a `for` loop or use `forEach()` to iterate over the items in the data set. Recall that the `data()` method parses the data set, and any method that's chained after `data()` is run once for each item in the data set.

**Challenge Instructions:**

Change the `x` attribute callback function so it returns the index times 30.

Note: Each bar has a width of 25, so increasing each `x` value by 30 adds some space between the bars. Any value greater than 25 would work in this example.

**My Solution:**

```Javascript 
<body>
  <script>
    const dataset = [12, 31, 22, 17, 25, 18, 29, 14, 9];

    const w = 500;
    const h = 100;

    const svg = d3.select("body")
                  .append("svg")
                  .attr("width", w)
                  .attr("height", h);

    svg.selectAll("rect")
       .data(dataset)
       .enter()
       .append("rect")
       .attr("x", (d, i) => {
         // Add your code below this line

return i*30;


         // Add your code above this line
       })
       .attr("y", 0)
       .attr("width", 25)
       .attr("height", 100);
  </script>
</body>

```
## Dynamically Change the Height of Each Bar

**The Lesson:**

The height of each bar can be set to the value of the data point in the array, similar to how the `x` value was set dynamically.

**Example:**

```Javascript 
selection.attr("property", (d, i) => {})

```
Here `d` would be the data point value, and `i` would be the index of the data point in the array.

**Challenge Instructions:**

Change the callback function for the `height` attribute to return the data value times 3.

**Note:** Remember that multiplying all data points by the same constant scales the data (like zooming in). It helps to see the differences between bar values in this example.

**My Solution:**

```Javascript 
<body>
  <script>
    const dataset = [12, 31, 22, 17, 25, 18, 29, 14, 9];

    const w = 500;
    const h = 100;

    const svg = d3.select("body")
                  .append("svg")
                  .attr("width", w)
                  .attr("height", h);

    svg.selectAll("rect")
       .data(dataset)
       .enter()
       .append("rect")
       .attr("x", (d, i) => i * 30)
       .attr("y", 0)
       .attr("width", 25)
       .attr("height", (d, i) => {
         // Add your code below this line

return d*3;

         // Add your code above this line
       });
  </script>
</body>
```
## Invert SVG Elements

**The Lesson:**

You may have noticed the bar chart looked like it's upside-down, or inverted. This is because of how SVG uses (x, y) coordinates.

In SVG, the origin point for the coordinates is in the upper-left corner. An x coordinate of 0 places a shape on the left edge of the SVG area. A y coordinate of 0 places a shape on the top edge of the SVG area. Higher x values push the rectangle to the right. Higher y values push the rectangle down.

To make the bars right-side-up, you need to change the way the y coordinate is calculated. It needs to account for both the height of the bar and the total height of the SVG area.

The height of the SVG area is 100. If you have a data point of 0 in the set, you would want the bar to start at the bottom of the SVG area (not the top). To do this, the y coordinate needs a value of 100. If the data point value were 1, you would start with a y coordinate of 100 to set the bar at the bottom. Then you need to account for the height of the bar of 1, so the final y coordinate would be 99.

The y coordinate that is `y = heightOfSVG - heightOfBar` would place the bars right-side-up.



**Example:**

```Javascript 

```

**Challenge Instructions:**

Change the callback function for the y attribute to set the bars right-side-up. Remember that the height of the bar is 3 times the data value d.

Note: In general, the relationship is `y = h - m * d`, where `m` is the constant that scales the data points.

**My Solution:**

```Javascript 
<body>
  <script>
    const dataset = [12, 31, 22, 17, 25, 18, 29, 14, 9];

    const w = 500;
    const h = 100;

    const svg = d3.select("body")
                  .append("svg")
                  .attr("width", w)
                  .attr("height", h);

    svg.selectAll("rect")
       .data(dataset)
       .enter()
       .append("rect")
       .attr("x", (d, i) => i * 30)
       .attr("y", (d, i) => {
         // Add your code below this line
return h-d*3;


         // Add your code above this line
       })
       .attr("width", 25)
       .attr("height", (d, i) => 3 * d);
  </script>
</body>
```

## Change the Color of an SVG Element

**The Lesson:**

The bars are in the right position, but they are all the same black color. SVG has a way to change the color of the bars.

In SVG, a `rect` shape is colored with the `fill` attribute. It supports hex codes, color names, and rgb values, as well as more complex options like gradients and transparency.



**Example:**

```Javascript 

```

**Challenge Instructions:**

Add an `attr()` method to set the fill of all the bars to the color navy.

**My Solution:**
```Javascript 
<body>
  <script>
    const dataset = [12, 31, 22, 17, 25, 18, 29, 14, 9];

    const w = 500;
    const h = 100;

    const svg = d3.select("body")
                  .append("svg")
                  .attr("width", w)
                  .attr("height", h);

    svg.selectAll("rect")
       .data(dataset)
       .enter()
       .append("rect")
       .attr("x", (d, i) => i * 30)
       .attr("y", (d, i) => h - 3 * d)
       .attr("width", 25)
       .attr("height", (d, i) => 3 * d)
       // Add your code below this line
 .attr("fill","navy"); 
 

       // Add your code above this line
  </script>
</body>

```

<img width="270" alt="Screenshot 2023-04-26 at 22 07 18" src="https://user-images.githubusercontent.com/19546253/234677882-98500745-74b1-4431-bb91-4229800cbbb3.png">


------

Copy below text as base for each lesson: 


## Add Document Elements with D3

**The Lesson:**

**Example:**

```Javascript 

```


**Challenge Instructions:**

**My Solution:**

```Javascript 

```
