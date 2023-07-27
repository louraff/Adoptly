# Adoptly

## Table of Contents

---

- [Description](#description)
- [Deployment Link](#deployment-link)
- [Code Installation Guide](#code-installation-guide)
- [Timeframe & Working Team](#timeframe--working-team)
- [Technologies Used](#technologies-used)
- [Brief](#brief)
- [Planning](#planning)
- [Build Process](#build-process)
- [Challenges](#challenges)
- [Wins](#wins)
- [Key Learnings & Takeaways](#key-learnings--takeaways)
- [Bugs](#bugs)
- [Future Improvements](#future-improvements)

## Description

---

Unleashing the full power of Django, JavaScript, HTML, CSS, and PostgreSQL, I introduce Adoptly, your digital best friend that connects you with your future furry friends. Developed in the final month of my journey at the General Academy Software Engineering Immersion course, Adoptly is a testament to late-night coding, a few too many coffees, and a deep desire to make pet adoption easier. Bridging the gap between pet seekers and homeless pets, this full-stack web application is a ‘pawfect’ encapsulation of what we learned - transforming data into dynamic pages and great user experiences. In essence, Adoptly is more than just a project, it's a labour of love and code, encapsulating the joys, challenges, and triumphs of our development journey.

![hero](/main_app/static/images/readme/gateway.png)
![formwizard](/main_app/static/images/readme/formwizard.gif)
![petprompt](/main_app/static/images/readme/petprompt.gif)

## Deployment Link

---

## Code Installation Guide

---

These instructions will help you get a copy of the project up and running on your local machine:

**Step 1: Clone the Repository**

To clone the repository to your local machine, open a terminal in your desired directory and use the following git command:

```bash
git clone https://github.com/louraff/Adoptly
```

\*_Step 2: Navigate into the Project Directory_

Switch to the project directory by entering the following command in the terminal:

```bash
cd Adoptly
```

**Step 3: Install the Dependencies**

Once inside the project directory, install the project's dependencies with:

```bash
pip install -r requirements.txt
```

**Step 4: Apply Migrations**

Apply the migrations to create the necessary database schema:

```bash
python manage.py migrate
```

**Step 5: Run the Development Server**

Finally, you can start the development server with:

```bash
python manage.py runserver
```

Open your web browser and navigate to http://127.0.0.1:8000/ to start exploring Adoptly!

Please note: This project was developed with Python 3.11, and while it should work on any version 3.6 or above, I recommend using Python 3.11 for the best compatibility.

## Timeframe & Working Team

---

This project was developed over the course of one week by a team of three developers: myself, Kyle, and Renad.

Here are the links to my team members' GitHub profiles, so you can check out their other awesome works:

[Kyle’s GitHub](https://github.com/KyleBarter) |
[Renad’s GitHub](https://github.com/renad1999)

## Technologies Used

---

For our project, we leveraged a variety of technologies across the frontend, backend, and various development and collaboration tools. Here's a detailed breakdown:

**Front End:**

HTML5: This is the standard markup language we used for structuring the pages of our web application.
CSS3: We used this for adding styles to the HTML elements, improving the user interface and experience.
JavaScript: It added dynamism and interactivity to the web pages.

**Back End:**

Python: Our primary programming language for backend logic.
Django: A high-level Python web framework that encourages rapid development and clean, pragmatic design.
SQLite: This served as our database system, where we stored and retrieved our application's data.

**Development Tools:**

GitHub: Used for version control and collaborative coding.
Visual Studio Code: My preferred code editor for this project.

**Collaboration and Planning Tools:**

Trello: Our project management tool, which helped us keep track of tasks and progress.
Quick Database Diagrams: This tool was used to create our ERDs
Slack: This was our primary communication tool throughout the project.

**Deployment:**

Fly.io: We deployed our application for public access using this platform.

## Brief

---

As part of our assignment, we were given a set of technical requirements to ensure we develop a full-stack Django application that not only aligns with best practices but also allows us to showcase a broad range of technical skills. Here is an overview of the brief:

**Technical Requirements:**

Be a full-stack Django application, demonstrating our ability to effectively use this Python-based web framework.

Connect to and perform data operations on a PostgreSQL database. We were instructed explicitly not to use the default SQLite3 database, emphasising the importance of working with more complex and robust databases in a real-world scenario.

Depending on whether we chose to consume an API, include at least one or two data entities (Models) in addition to the built-in User model, which were to form either a one-to-many (1:M) or a many-to-many (M:M) relationship.

Include full-CRUD (Create, Read, Update, Delete) data operations across any combination of the app's models, excluding the User model. This challenged us to ensure our application could handle a variety of data manipulations for enhanced functionality.

Authenticate users using Django's built-in authentication, ensuring the privacy and security of user data.

Implement authorisation, restricting access to the Creation, Updating & Deletion of data resources, thus ensuring appropriate access controls were in place.

Be deployed online using Heroku, underlining the need for web deployment skills.

**Optional features:**

Upload images to AWS S3, expanding our experience with cloud storage services.

Consume an API, requiring us to install and use the Requests package.

**Other requirements:**

Finally, as part of our teamwork and collaboration requirements, we were expected to manage team contributions using the Git/GitHub team workflow, ensuring each team member made significant contributions to the project via git commits.

This brief served as a comprehensive guide, allowing us to develop an application that not only meets educational requirements but also prepares us for similar projects we may encounter in our future roles.

## Planning

---

The first steps in our project revolved around defining roles and brainstorming concepts. Our team designated specific roles for each member. I took the lead as the Scrum Master and designer, while Kyle was entrusted as our GitHub Manager and Database Manager, and Renad acted as the Documenter.

As the team's designer, I was inspired by the intuitive and appealing UX/UI of the Hinge app and saw an opportunity to infuse a similar design philosophy into the pet adoption process. I proposed that our app should prioritise the personality and temperament match between potential pet owners and pets. This approach aimed to revolutionise the often shallow, appearance-based criteria prevalent in such decisions. I firmly believed that our app needed to be more than just a transactional platform, unlike what we observed in other apps like Pets4Homes which feels like an Ebay for pets. Instead, I envisioned our app as a journey, a path leading users to fall in love with their ‘pawfect’ pet match.

The following images showcase the wireframes I created for our project:

![Wireframes](/main_app/static/images/readme/adoptly-wireframe.png)

One of the first tasks after establishing roles and app concept was to craft user stories. This responsibility fell on my shoulders, and I designed them to guide our development process. Each story represented a specific functionality or feature that our end-users would require from our app. They later served as a roadmap, helping us assign coding tasks and track our progress.

When it came to our database structure, our ERDs played a crucial role in showcasing the relationships between different data entities within our application. Renad did a fantastic job creating the ERD, which we reviewed and edited as a team.

![ERD](/main_app/static/images/readme/adoptlyerd.png)

As the Scrum Master, I was in charge of our Trello board, which I managed diligently to ensure our workflow remained smooth and efficient. I took the helm in leading our standups, merge parties, and sprints, facilitating a collaborative and proactive atmosphere within the team. We were all conscious about being adaptable, knowing our approach might need to evolve for maximum efficiency.

With a clear vision and thorough planning in place, each of us naturally aligned with aspects of the app that resonated with us. The matching algorithm, in particular, piqued my interest. I took ownership of this feature and initiated its development by writing pseudocode. The algorithm had a complexity of O(n), which meant we'd be performing operations linearly with the number of pets, under the assumption that comparison operations were constant. This seemed reasonable, considering the nature of our scoring system.

Kyle, as the Database Manager, was pivotal in setting up our database and Git repo, while Renad, as the Documenter detailed our ERDs and acted as our researcher. With everyone pulling their weight and me steering the team, we concluded our planning phase with a strong, shared vision of what our app would look like, its flow, and its unique matching functionality. This clarity laid a solid foundation as we embarked on the coding phase of our app.

## Build Process

---

**Initial Stages and Form Wizards**

The first few days were dedicated to setting up the match functionality, which relied heavily on the questions asked of the pet adopters and pet owners upon sign-up. We quickly decided to use Django’s form wizard functionality because we wanted to present a series of questions to the user, one at a time, without the page reloading. We split the task between Renad and myself - Renad worked on the adopter's form wizard, while I tackled the pet owner's form wizard.

Form wizards presented a new challenge as we hadn't been taught this functionality, leading us to rely heavily on reading and understanding the documentation to implement them with the envisioned look. This task occupied a significant part of the initial days, but it was a learning curve that equipped us with a deeper understanding of Django Form Wizards.

![Form Wizard Demo](/main_app/static/images/readme/formuntilprompt.gif)

While Renad and I were engrossed with the form wizards, Kyle took on building the matches and likes pages, ensuring a division of labour that capitalised on our individual strengths.

**Mid-Stages: Matching Algorithm and Styling**

Once the form wizards were in place, my focus shifted to developing the matching functionality. This feature was central to our application's main goal: finding the 'pawfect' match based on user preferences. Simultaneously, I dedicated considerable time to the application's styling, working towards a uniform and aesthetic UI across all pages.

##### Views.py, 75-104:

```python
def find_matches(request):
    user, created = AdoptionPreferences.objects.get_or_create(user=request.user)
    pets = PetTable.objects.all()
    matches = []
    print(user)
    pets = PetTable.objects.all()
    print(f"Total pets: {len(pets)}")
    matches = []
    for pet in pets:
      score = 0
      if user.activityLevel == pet.activity_level:
          score += 1
          print(f"{pet.name} matches activity level")
      if user.sociability == pet.sociability:
          score += 1
          print(f"{pet.name} matches sociability")
      if user.size == pet.size:
            score += 1
            print(f"{pet.name} matches size")
      else:
            print(f"{pet.name} does not match size. User's size preference: {user.size}, Pet size: {pet.size}")

      if score >= 2:
        matches.append((pet)) #Append the pet and its score as a tuple
        print(f"Added {pet.name} to matches")
        # sorted_matches = sorted(matches, key=lambda x: x[1], reverse=True) #Sort by score in a descending order
        # sorted_pets = [pet for pet, score in sorted_matches] #Extract sorted pets
        print(f"Score for pet {pet.id} ({pet.name}): {score}")
    print(f"Total matches: {len(matches)}")
    return matches
```

In the find_matches function, I first retrieve the user's adoption preferences using Django's get_or_create function. The real fun starts with iterating over each pet and scoring them based on how closely they match the user's preferences in terms of activity level, sociability, and size. This process is implemented using a simple scoring system where each match contributes a score of '1'.

One design decision here was to consider any pet with a score of 2 or higher as a match, and append it to the matches list. This decision was based on the premise that users would prefer pets that match at least two out of three preferences. I also made sure to print useful debugging information throughout, which was invaluable for testing and validation.

Meanwhile, Renad focused on building the settings/about page, further enhancing the user experience and the application's functionality. Our collaborative approach ensured progress across multiple fronts, making our work more efficient.

**Final Stages: Database Population and Authentication**

Creating a vast and varied database for an application like Adoptly is a time-consuming task if done manually. So, I wrote a custom Django command to automate this process. This command made use of the Python 'faker' library to generate fake pet details, such as names, ages, breeds, and more. It also leveraged the 'requests' library to fetch random dog images from an external API, providing each pet profile with a unique set of images. This worked out ridiculously well and provided ample entertainment to get me through the last stages of the project. I wouldn’t deny my reader a giggle so here’s an example of the fruits of my database population…

![Example Pet](/main_app/static/images/readme/pet200.png)

The command could be run in the Django shell, which would trigger the generation of a specified number of pet profiles, each randomly different from the others. This not only saved us an immense amount of time but also allowed us to simulate a real-world scenario where our application would have a vast database of pets to match with users. This feature allowed us to demonstrate the match functionality effectively and added realism to our testing process.

Create_fake_data.py

```python
class Command(BaseCommand):
    help = 'Create random dogs'

    def handle(self, *args, **options):
        # Deleting existing pets.
        PetTable.objects.all().delete()

        fake = Faker()
        user = User.objects.first()  # Using first user for simplicity

        for _ in range(100):
            pet = PetTable(
                user=user,
                name=fake.first_name(),  # Generates only first name
                gender=choice(GENDER_CHOICES)[0],
                sociability=choice(SOCIABILITY_CHOICES)[0],
                age=fake.random_int(min=1, max=10),
                breed=fake.word(),
                size=choice(SIZE_CHOICES)[0],
                weight=fake.random_int(min=1, max=100),
                healthStatus=choice(HEALTH_STATUS_CHOICES)[0],
                activity_level=choice(ACTIVITY_LEVEL_CHOICES)[0],
                energy_level=choice(ENERGY_LEVEL_CHOICES)[0],
                vaccinationInformation=choice(VACCINATION_CHOICES)[0],
                monthlyCost=fake.random_int(min=50, max=500)
            )
            pet.save()

            # Saving 3 images for each pet
            for _ in range(3):
                response = requests.get('https://dog.ceo/api/breeds/image/random')
                image_url = response.json()['message']

                pet_image = PetImage(
                    url=image_url,
                    pet=pet
                )
                pet_image.save()

            for i in range(3):
                prompt = Prompt(
                    prompt=choice(PROMPT_CHOICES)[0],
                    answer=fake.sentence(),
                    pet=pet
                )
                prompt.save()

```

Each iteration fetches a random dog image from the 'dog.ceo' API and saves it in association with the created pet, enhancing the visual aspect of the data and emulating real-world scenarios.

The command creates 100 random dogs, each with various characteristics like name, gender, and age, generated using the Faker library for realistic but fictitious data. These characteristics are selected with a mix of random choices and ranges, simulating the diversity you'd expect in a real pet adoption context.

I also incorporated user authentication into our web application, an essential aspect of securing our users' data and providing a personalised experience.

During these last stages, we had to deal with a number of bugs that arose during merging and the integration of different features. Debugging was an iterative process, but we managed to resolve most of the issues, improving the stability and functionality of our app, Adoptly.

**Project Wrap-up**

Despite not completing the application entirely within the given timeline, our team worked diligently and passionately to get Adoptly to its current state. We believe in the potential of our idea and are proud of the work we've accomplished so far.

## Challenges

---

In our journey to bring Adoptly to life, I encountered a mix of leadership, team management, and technical challenges. Each obstacle provided a rich opportunity for learning and growth. Here's how I tackled them:

### Leadership and Team Management Challenges

As the team lead, I grappled with several challenges inherent to this role. Among my key responsibilities was the task of distilling and simplifying our ambitious concept for Adoptly. The team initially envisioned a platform featuring multiple animal types, advanced filters, and a nearby shelters map. However, considering our limited time and resources, these features were beyond our project's scope.

Leveraging my leadership skills, I steered our team towards a more realistic goal through open and fluid communication. We successfully scaled down the concept, relegating complex features to stretch goals.

However, communication wasn't always smooth. We hit a road bump when a team member underestimated the complexity of the 'matches' and 'likes' pages, leading to a scramble towards the end of the project. This incident underscored the importance of closely tracking project progress and not just relying on verbal updates. It was a pivotal learning experience for me as a leader.

I chose to maintain a positive attitude and rallied the team to solve the problem collaboratively. This morale boost invigorated the team, motivating everyone to give their best during the project's final stages.

### Technical Challenges

**Form Wizards and Styling:**

One of the significant technical challenges was customising the form wizards to match my vision for Adoptly. The default form wizards needed styling and lots of customisation. It became clear that the task of customising these forms felt like hitting a brick wall of untouchable code.

```html
  <form method="post" enctype="multipart/form-data">
        {% csrf_token %} {{ wizard.management_form }}
        {% if wizard.form.forms %} {{ wizard.form.management_form }}
        {% for form in wizard.form.forms %}
        {% for field in form %}
          <label for="{{ field.id_for_label }}">{{ field.label }}</label>
          {{ field.errors }} {{ field.help_text }} {{ field }}
        </div>
        {% endfor %}
        {% endfor %}
        {% else %} {{ wizard.form }} {% endif %}
        <input type="submit" value=">"/>
      </form>
```

This code snippet is the HTML template I used to render the form wizards for eight different forms in my application. It may look like a simple HTML form with some Django template tags sprinkled in, but oh, how appearances can deceive!

Styling these form wizards felt akin to knitting with boxing gloves on. With little CSS to latch onto, the task began to seem like an attempt to catch smoke with a net. My greatest adversary? An innocuous-looking label that, for some reason, simply refused to be grabbed on to. It was one slippery fish.

![difficult label](/main_app/static/images/readme/devilslabel.png)

I'd had some previous success styling labels using CSS attribute selectors, targeting them like so:

```css
label[for=energy_level_1]
```

This allowed me to zero in on specific labels and bestow upon them the desired styling. However, our rogue label was not swayed by such techniques. It clung to its original style, unmoved by my pleas for uniformity. Styling wise, this really needed to be fixed. I've added before and after pics for you to grasp the gravity of this problem.

Before styling that pesky label:
![before styling](/main_app/static/images/readme/petbefore.png)

After styling the label:
![after styling](/main_app/static/images/readme/petafter.png)

My search for a solution took me deep into the labyrinth of Django's documentation and to the outer limits of Stack Overflow. But even after hours of reading and experimenting, that stubborn label remained unstylable, mocking my attempts with the apathy only an HTML element can muster.

In a state of semi-despair, I sought the help of my course instructor. Together, we spent a hair-pulling two hours, wrestling with the obstinate label, our screens reflecting our determined, squinted expressions.

Finally, like a pair of digital MacGyvers, we managed to apply a bit of CSS hackery to wrangle the label into submission.

```css
form>label
```

![css hack](/main_app/static/images/readme/hackery.png)

Although the final solution was a tad hacky and wouldn't win any beauty contests in the code world, it did the trick.

I'm still on the hunt for a more elegant solution, ever vigilant for that elusive answer that's bound to be lurking in the depths of the Django-verse.

Here’s a snippet of code I wrote that demonstrates more of the customisation process I went through for each form:

```python
class PetForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'age': forms.NumberInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
        }
        labels = {
            'name': _('Pet Name'),
            'age': _('Age'),
            'description': _('Description'),
        }
```

The code snippet demonstrates two key aspects of my customisation process. The widgets dictionary allowed me to specify the visual representation of data fields. I associated each field with the corresponding form control type (TextInput, NumberInput, and Textarea) and applied CSS classes for additional style control.

The labels dictionary, on the other hand, served to redefine the standard field labels with more user-friendly descriptions. This not only helped enhance the user experience but also further customised the appearance of the form fields to align with the application's aesthetic.

**Database Population through Custom Command Code:**

I knew there must be a faster way of populating our database that didn’t involve manually creating hundreds of dog profiles. I asked ChatGPT if there was a quick way to do this and the response pointed me in the direction of Django’s custom management command: “You can write a script that creates Dog instances and saves them to the database. This script can be part of a Django custom management command so you can run it from the command line whenever you need to generate the data.”

I carefully read Django’s documentation on custom django-admin commands and found it was exactly what I didn’t know I needed. I also found an API called Dog CEO’s Dog API for random dog images and settled on the Faker library for random text and formulated my command.

After writing and running the custom command, I encountered an error indicating the absence of the 'requests' module. I subsequently installed it separately using pip since it isn't part of Python's standard library. The way I originally coded the command meant only one image was uploading for each pet profile and pets were given first and second names, so I added a few modifications to attach three images to each pet and to only give them first names. I made the necessary adjustments, ensuring to delete all existing pets before creating new ones.

**Bugs and Errors:**

Software development invariably involves bugs and errors, and our project was no exception. Various bugs emerged during development, especially concerning image uploading and model migrations. Additionally, the frontend development of the home and matches pages wasn't up to the standard of the rest of the app, hampering backend functionality. As a team, we handled these situations through thorough testing and collaborative problem-solving.

**Benefits:**
Each challenge surmounted made Adoptly more robust. Customising the form wizards led to a sleek user interface, and writing a custom database population command enhanced our data richness and variety. Additionally, overcoming hurdles together cemented our team dynamic and honed our individual problem-solving skills. These challenges didn't just shape Adoptly but also fueled our growth as software engineers.

## Wins

---

It is no secret that the development of Adoptly posed several challenges. Still, through resourcefulness and a relentless problem-solving approach, I transformed my challenges into notable achievements:

**Base Command Data Population Code**
A standout accomplishment I am particularly proud of is the creation of a custom Django command to automate the population of our database with mock data. This command revolutionised our testing and debugging workflows, allowing us to swiftly pinpoint and rectify issues.

Crafting this command wasn't without hurdles - from grappling with the appropriate file structure to addressing non-standard Python dependencies. Yet, overcoming these challenges enriched my understanding of Django's powerful functionalities and underscored the essence of diligent research and problem-solving. Furthermore, this tool significantly accelerated our development timeline, simulating real-world scenarios with a vast pet database, which in turn added realism to our testing process and effectively demonstrated the match functionality.

Below is a screenshot of the matches page with a list of pets that have been matched with that user:

![matches page](/main_app/static/images/readme/matchespage.png)

**Consistent Hard Work and Focus**
Despite the rigorous demands of Adoptly's development, I maintained a high level of dedication and focus. I consistently met and often exceeded expectations, delivering high-quality work under tight deadlines. I am particularly proud of my ability to concentrate during crucial phases of the project, ensuring that all tasks assigned to me were completed accurately and on time. As a result, I coded the pet profile creation using Form Wizards and AWS for image uploading, wrote a custom Django command to automate the population of our database with mock data, I also incorporated user authentication, implemented full CRUD functionality and wrote our matching algorithm whilst supporting my teammates with bugs and blocks.

**Visual Design**
Another achievement that fills me with pride is the significant role I played in shaping Adoptly's visual identity. I took the lead in designing various key pages - from the form wizards and sign-up/login pages to the landing page. These designs elevated the user experience and helped manifest our team's vision for the application, aligning aesthetics with functionality. My styling did not stretch to the matches/likes/settings pages. Here are a few of the pages I coded and styled:

![hero](/main_app/static/images/readme/gateway.png)
![login page](/main_app/static/images/readme/login.png)
![pet form](/main_app/static/images/readme/petafter.png)
![pet profile](/main_app/static/images/readme/pet200.png)

**Teamwork and Patience**
Finally, I am proud of how I collaborated with my team members during tense and frustrating moments towards the end of the project. I consistently encouraged open communication and patience, which not only helped maintain a positive atmosphere but also fostered an approach to overcoming bugs and problems in our code with collaborative problem-solving and good old-fashioned determination. Maintaining patience and keeping morale high during challenging periods was a significant win for both myself and the team.

## Key Learnings & Takeaways

---

The Adoptly project was a substantial stepping-stone in my development as a software engineer. It presented an array of learning opportunities that refined my technical and leadership skills. Here are some of the key learnings:

Project Management Practices: Embarking on this journey, the first significant challenge was efficient project management. In an effort to create a harmonious and productive team environment, I adopted practices like standups, pair programming, and efficient division of tasks. I learned that being adaptive and open-minded is essential to successfully work in a team and ensuring we are always evolving to be more efficient, collaborative and creative in our build process.

Leadership Skills: As the team lead for Adoptly, I faced an array of challenges that demanded effective communication, realistic goal setting, and vigilant oversight of the project's progress. I learned to create space for ideas to flow and how to build confidence in less formidable members of the team to ensure we were getting the best out of every team member. Additionally, regularly reviewing the code as a means to track project and individual progress rather than relying solely on verbal updates will be a key learning I take into my next group project. This experience significantly enhanced my leadership skills, preparing me for future roles that demand taking charge.

Mastery of Django Form Wizards and Django ORM: Technically, this project afforded me the opportunity to delve deeper into Django's capabilities. Customising form wizards to meet our specific needs and creating separate models for prompts, I improved the efficiency and optimization of our database schema. This practical exploration reinforced my understanding of Django ORM, allowing me to solve complex challenges like creating a personalized user journey through our application.

Automated Data Generation: Lastly, I learned how to automate data population using Django’s Base Command. This tool automated the generation of mock data, enabling rapid testing and development.

## Future Improvements

---

Fix Existing Bugs: Squash 'em all! Like a pesky mosquito, I aim to hunt down and eliminate all current bugs, leading to a more pleasant user experience.

Styling: Implementing the wireframe styling for the matching and likes pages is on the cards, along with giving the navbar a much-needed glow-up.

Screen Compatibility: I plan on ensuring that the app looks and functions impeccably across devices, not just mobiles, because pet love knows no bounds (or screen sizes)

Skipping the Questionnaire: Sometimes, we just know what we want. Users should have the option to skip the questionnaire and head straight into viewing pets.

Advanced Filtering: I plan to offer the option to refine pet matches based on specific pet characteristics. Like dating, finding your pet match should also be about finding the right 'type'.

Location Mapping: We'll help you plot your route to pet love, with integrated maps showing the location of potential pet matches or shelters.

In-app Chat: Wouldn't it be great if you could just chat with the shelter or pet owner and organise a visit?

Notifications: Fast replies win hearts. I would love for users to receive notifications when someone replies to your chat.

One-at-a-time Pet Profiles: Instead of seeing an index of pet matches, I would love for users to have a more interactive experience with finding their pawfect pet. Swiping through potential pet matches one at a time? It's like Tinder but way cuter!
