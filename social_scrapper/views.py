from django.shortcuts import render

# Create your views here.


def HelloWolrd(request):
    context = """
    Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Et netus et malesuada fames ac turpis egestas. Malesuada fames ac turpis egestas sed tempus urna et pharetra. Quis commodo odio aenean sed adipiscing diam donec adipiscing tristique. Nullam non nisi est sit amet. Elit ullamcorper dignissim cras tincidunt lobortis feugiat. Eu nisl nunc mi ipsum faucibus vitae aliquet nec ullamcorper. Nibh cras pulvinar mattis nunc sed blandit libero volutpat. Quam elementum pulvinar etiam non. Est sit amet facilisis magna etiam. Elementum sagittis vitae et leo duis ut diam quam nulla. Nunc sed velit dignissim sodales ut eu sem integer vitae. Porttitor leo a diam sollicitudin tempor id eu nisl nunc. Non blandit massa enim nec dui.

Neque convallis a cras semper auctor. In cursus turpis massa tincidunt dui ut ornare lectus. Ac orci phasellus egestas tellus rutrum tellus pellentesque eu. Malesuada fames ac turpis egestas integer eget aliquet nibh praesent. Nam at lectus urna duis convallis convallis tellus. Mauris augue neque gravida in. Ipsum a arcu cursus vitae congue. Sapien faucibus et molestie ac feugiat sed lectus vestibulum. Nunc sed blandit libero volutpat sed cras ornare arcu. Sed id semper risus in hendrerit gravida rutrum. Facilisi nullam vehicula ipsum a arcu. Gravida neque convallis a cras semper auctor neque vitae. Enim facilisis gravida neque convallis a. Elementum curabitur vitae nunc sed velit dignissim sodales. Aliquet enim tortor at auctor urna nunc id. Fusce ut placerat orci nulla pellentesque dignissim enim sit. Tellus in hac habitasse platea dictumst vestibulum. Ac tincidunt vitae semper quis lectus nulla at volutpat. Feugiat pretium nibh ipsum consequat nisl vel pretium lectus. Purus sit amet luctus venenatis lectus.
    
    """
    return render(request, 'social_scrapper/index.html', {'content': context})




