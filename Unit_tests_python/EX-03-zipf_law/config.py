from ChatGPT import zipfs_law as ChatGPT
from CodeLLama import zipfs_law as CodeLLama
from Bard import zipfs_law as Bard
from Perplexity import zipfs_law as Perplexity
from Claude import zipfs_law as Claude
from Copilot import zipfs_law as Copilot

# Define the implementations with their names
implementations = [
    (ChatGPT, 'ChatGPT'),
    (CodeLLama, 'CodeLLama'),
    (Bard, 'Bard'),
    (Perplexity, 'Perplexity'),
    (Claude, 'Claude'),
    (Copilot, 'Copilot')
]

string_input = '''toward it, and then stopped.

There was a sound. A soft sliding sound. It stopped, then started again with a stealthy little bump. Everything inside me went loose. I regressed magically to four years of age. That sound wasn’t coming from the market. It was coming from behind me. From outside. Where the mist was. Something that was slipping and sliding and scraping over the cinderblocks. And, maybe, looking for a way in.

Or maybe it was already in, and it was looking for me. Maybe in a moment I would feel whatever was making that sound on my shoe. Or on my neck.

It came again. I was positive it was outside. But that didn’t make it any better. I told my legs to go and they refused the order. Then the quality of the noise changed. Something rasped across the darkness and my heart leaped in my chest and I lunged at that thin vertical line of light. I hit the doors straight-arm and burst through into the market.

Three or four people were right outside the double doors—Ollie Weeks was one of them—and they all jumped back in surprise. Ollie grabbed at his chest. “David!” he said in a pinched voice. “Jesus Christ, you want to take ten years off my—” He saw my face. “What’s the matter with you?”

“Did you hear it?” I asked. My voice sounded strange in my own ears, high and squeaking. “Did any of you hear it?”

They hadn’t heard anything, of course. They had come up to see why the generator had gone off. As Ollie told me that, one of the bag-boys bustled up with an armload of flashlights. He looked from Ollie to me curiously.

“I turned the generator off,” I said, and explained why.

“What did you hear?” one of the other men asked. He worked for the town road department

; his name was Jim something.

“I don’t know. A scraping noise. Slithery. I don’t want to hear it again.”

“Nerves,” the other fellow with Ollie said.

No. It was not nerves.

“Did you hear it before the lights went out?”

“No, only after. But...” But nothing. I could see the way they were looking at me. They didn’t want any more bad news, anything else frightening or off-kilter. There was enough of that already. Only Ollie looked as if he believed me.

“Let’s go in and start her up again,” the bag-boy said, handing out the flashlights. Ollie took his doubtfully. The bag-boy offered me one, a slightly contemptuous shine in his eyes. He was maybe eighteen. After a moment’s thought, I took the light. I still needed something to cover Billy with.

Ollie opened the doors and chocked them, letting in some light. The bleach cartons lay scattered around the half-open door in the plywood partition.

The fellow named Jim sniffed and said, “Smells pretty rank, all right. Guess you were right to shut her down.”

The flashlight beams bobbed and danced across cartons of canned goods, toilet paper, dog food. The beams were smoky in the drifting fumes the blocked exhaust had turned back into the storage area. The bag-boy trained his light briefly on the wide loading door at the extreme right.

The two men and Ollie went inside the generator compartment. Their lights flashed uneasily back and forth, reminding me of something out of a boys’ adventure story—and I illustrated a series of them while I was still in college. Pirates burying their bloody gold at midnight, or

maybe the mad doctor and his assistant snatching a body. Shadows, made twisted and monstrous by the shifting, conflicting flashlight beams, bobbed on the walls. The generator ticked irregularly as it cooled.

The bag-boy was walking toward the loading door, flashing his light ahead of him. “I wouldn’t go over there,” I said.

“No, I know you wouldn’t.”

“Try it now, Ollie,” one of the men said. The generator wheezed, then roared.

“Jesus! Shut her down! Holy crow, don’t that stink!”

The generator died again.

The bag-boy walked back from the loading door just as they came out. “Something’s plugged that exhaust, all right,” one of the men said.

“I’ll tell you what,” the bag-boy said. His eyes were shining in the glow of the flashlights, and there was a devil-may-care expression on his face that I had sketched too many times as part of the frontispieces for my boys’ adventure series. “Get it running long enough for me to raise the loading door back there. I’ll go around and clear away whatever it is.”

“Norm, I don’t think that’s a very good idea,” Ollie said doubtfully.

“Is it an electric door?” the one called Jim asked.

“Sure,” Ollie said. “But I just don

't think it would be wise for—”

“That’s okay,” the other guy said. He tipped his baseball cap back on his head. “I'll do it.” '''

first_6_words = ['the','i','and','it','of','was']
valid_7th8th_words = ['a','in'] # any order
valid_9th10th_words = ['that','ollie', 'said'] # any order

def get_implementations():
    return implementations

def get_string_input():
    return string_input