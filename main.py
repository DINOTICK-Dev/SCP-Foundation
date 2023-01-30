"""
Made by DINOTICK
Please do not sell or claim my code as your own
ASCII: █ (219)
"""

import scpscraper as scpscraper
from colorama import init
from termcolor import colored
import time
import sys
import climage

def StartupDialog():
  print(colored("Booting fans...", "cyan"))
  time.sleep(0.5)
  print(colored("Loading hard-drive...", "cyan"))
  time.sleep(0.5)
  print(colored("Powering CPU...", "cyan"))
  time.sleep(0.25)
  print(colored("Loading User-Information...", "cyan"))
  time.sleep(0.2)
  print(colored("Welcome, Dr. ███████", "cyan"))
  time.sleep(0.35)
  print(colored("Password:", "cyan"))
  time.sleep(0.2)
  print(colored("█████████████", "cyan"))
  time.sleep(0.3)
  print(colored("Authenticating with the FOUNDATION...", "cyan"))
  time.sleep(0.2)
  print(colored("Successfully authenticated credentials.", "green"))
  time.sleep(0.1)
  print(colored("Welcome Dr. ███████, happy researching!", "cyan"))
  time.sleep(0.3)
  print(colored("Loading SCP Database...", "cyan"))
  time.sleep(0.1)
  print(colored("SCP Safe: Loaded!", "green"))
  time.sleep(0.1)
  print(colored("SCP Euclid: Loaded!", "green"))
  time.sleep(0.1)
  print(colored("SCP Keter: Loaded!", "green"))
  time.sleep(0.1)
  print(colored("SCP Thaumiel: Loaded!", "green"))
  time.sleep(0.1)
  print(colored("SCP Neutralized: Loaded!", "green"))
  time.sleep(0.1)
  print(colored("SCP Apollyon: Loaded!", "green"))
  time.sleep(0.1)
  print(colored("SCP Archon: Loaded!", "green"))
  time.sleep(0.25)
  print(colored("MTF Personnel... Loaded!", "green"))
  time.sleep(0.5)
  print(colored("Scientist Personnel... Loaded!", "green"))
  time.sleep(0.2)
  print(colored("Security Personnel... Loaded!", "green"))
  time.sleep(0.75)
  print(colored("All systems: OK\nWelcome to the public SCP Database, Dr. ███████.", "cyan"))

#StartupDialog()

while True:
  scpinput = input(colored("\nWhat would you like to search for?\n({SCP Number}=Information on a specific SCP)\n(DR=Information on Doctors)\n(MTF=Information on MTF Personnel)\n(DC=Information on D Class Personnel)\n(RC=Information on Researcher Personnel)\n(DI=Information on Director Personnel)\n(SC=SCP Objects of interest)\n> ", "cyan")).lower()
  if scpinput == "mtf":
    print(colored("""Mobile Task Forces (MTFs) are elite units comprised of personnel drawn from across the Foundation and are mobilized to deal with specific threats or situations that sometimes exceed the operational capacity or expertise of regular field personnel and — as their name suggests — may be relocated between facilities or locations as they are needed. Mobile Task Force personnel represent the "best of the best" of the Foundation.

Mobile Task Forces vary greatly in size, composition, and purpose. A battalion-strength combat-oriented task force trained to deal with highly aggressive anomalous entities may consist of hundreds of troops plus support personnel, vehicles, and equipment and can be deployed in whole or in part to deal with threats across the globe. However, a Mobile Task Force can also be a small, specialized intelligence-gathering or investigative task force that may have fewer than a dozen personnel if that is deemed sufficient to accomplish their goals.

While in the field, task force members often pose as emergency responders, local or federal law enforcement, or military personnel appropriate to the region in which they are operating. Mobile Task Force Commanders can also request the assistance of local field units or personnel stationed at nearby Foundation facilities in order to accomplish their missions.


ORGANIZATION

Each unit is fundamentally structured in a way that best suits their intended purpose. While combat-oriented task forces may closely follow military hierarchy and organization, smaller units may have an informal or otherwise esoteric chain of command. As such, the responsibilities of the Mobile Task Force Commander (MTFC) for each particular task force can vary greatly; the commander for a large task force might focus on maintaining multiple teams and deploying them as necessary to each assigned operation, whereas the commander of a small team might deploy with their team and direct the operation from on location.

Similarly, the cohesion of each unit will vary as well. Some Mobile Task Forces consist of personnel who have trained and worked for many years or even decades together, whereas the personnel of a Mobile Task Force formed on a moment's notice to deal with a specific incident may know little more than each others' names and fields of expertise.


CREATION

Mobile Task Forces are typically commissioned as deemed necessary by the Foundation's Director of Task Forces, often with the direct approval of one or more O5 Council members. A significant number of Mobile Task Forces are created to deal with specific anomalies exhibiting traits that standard containment or response teams are unable to effectively counteract, though many were also created to pre-empt an emerging or theoretical threat.


DEACTIVATION

Mobile Task Forces created for the purpose of containing a particular anomaly are typically deactivated at the end of the recovery operation or when ongoing containment is deemed no longer necessary. Occasionally, such task forces remain operational if the expertise and experiences learned are considered useful for future incidents, but otherwise the task force will likely be disbanded and its personnel returned to their prior posts. Very rarely, a Mobile Task Force will also be disbanded if it suffers sufficient casualties to render it incapable of operation. In these cases, if the prior capability of that particular task force is deemed necessary, a new task force may be commissioned to replace it.""", "green"))
  if scpinput == "dr":
    print(colored("""Dr. Daniel Asheworth: Thaumaturgist and self-proclaimed alchemist. Hot-headed, short-tempered, and sometimes arrogant, but with a good heart. Born from an unknown American mother and an unknown Polish father in the late 1950s. One of few people in the Foundation capable of prolonging their youth through anomalous means.

Lead of the Damien Nowak Case. Believed to once have had been a temporary member of the Wanderers' Library and Wilson's Wildlife Solutions, Daniel Asheworth has proven numerous times to be a useful asset in Site-120's Director Council.

All magic comes with a price...
Doctors Thomas, Trevor and Tristan Bailey: Identical triplets employed by the Foundation. Sons of Tyler Bailey, inventor of the Multi-Universal Transit Array. Employed by the Foundation for an unknown period of time (employee records and personal accounts differ), and look anywhere between 20 and 40 as a side effect of constantly crossing universal barriers.

Trevor Bailey is the former head of the Department of Multi-Universal Affairs, before being demoted to a desk job at Site-19 for mishandling of a Keter-class anomaly. Tom “Bombadill” Bailey is currently the commissioner of Site-1483 (within the Third Antarctic Empire), following a career spent exploring alternate universes. Tristan Bailey is a physicist, diplomat and designer of a multi-universal translator. Formerly assigned to [REDACTED], currently stationed at Site-87.

Dr. Harold Blank: An historian of anomalous phenomena, Chair of Archives and Revision at Site-43. Grumpy, sarcastic, incapable of taking anything more seriously than it needs to be taken, including himself. One of a select few staff at his Site forced to navigate alternate timelines every time he fucks up one specific duty on one specific day each year. "Friends" with Dr. Wettle, best friends with Dr. Lillihammer and romantically linked with research partner Dr. Melissa Bradbury.

History is written by...
Dr. Django Bridge: Foundation Archivist. Quiet but influential, with a touch of both melancholy and whimsy. Extraordinary memory. On a first-name basis with Dr. Bright, and has frequently acted as an informal assistant for him.

Dr. Jack Bright: Director of Foundation Personnel. Somewhat amoral. Extremely loyal to the Foundation. May be ridiculous, may be terrifying; is certainly blunt. Attached to SCP-963, and is therefore immortal, using the body of whatever SCP-963 has last touched.

I've been with the company for a long time.
Dr. Jeremiah Cimmerian: An ethics committee liaison that takes his job only somewhat seriously. He never thought his doctorate in English Literature or his minor in philosophy would actually help him stay employed, but the former got him recruited into the Foundation as a researcher and the latter secured his employment in the long term. Has an unusual interest in puns and the ethical treatment of humanoids.

Dr. Alto Clef: Enigmatic and genre-savvy. A highly adaptable, clever liar. Former Global Occult Coalition (GOC) operative, specializing in reality benders. Also a former file clerk. Undergone anomalous alterations that provide resistance to reality shifts and prevent his face from being photographed. Has a long and checkered history, a flair for the dramatic, and a somewhat hidden streak of self-hatred. Reformed misogynist. Most rumors about him are exaggerated or off-point.

They'll say anything about me.
Dr. Kain "Pathos" Crow: Cross-disciplinary wunderkind researcher, specializing particularly in biochemistry and robotics. Rarely, if ever, seen in public. May or may not have been permanently transformed into a dog-like body as the result of a particular anomalous event.

I'm so tired these days.
Dr. Dan ███████: Insufferable, emotive genius with a big-picture-centric set of principles. Former marine. Lead researcher on an SCP too dangerous to keep around, but couldn't make the O5 Council see it that way. Took matters into his own hands, getting dozens of people killed, getting his decommissioning request accepted, and getting a death sentence (in that order).

You make one little mistake...
Dr. Michael Edison: Level-3 Researcher, current head of the Foundation's Inter-Site Testing Initiative (ISTI). Dr. Edison has received disciplinary action on multiple occasions due to a repeated pattern of unsanctioned and ill-conceived behavior. These behaviors have resulted in temporary reassignment to the Site-██ Antarctic base. His current assignment at Site 19 is contingent on approval from his assigned therapist.

My legends begins in the 12th century...
Dr. Chelsea "Photosynthetic" Elliott: Plant specialist, both anomalous and non-anomalous. Dedicated, friendly, prone to tunnel vision. Often in the field; excessively 'hands-on' in her lab and field research, leading to a number of injuries. Scars cover her hands and arms.

We're at the cusp of something here.
Dr. Justine 'Jay' Everwood: GoI specialist, very well-read and knowledgeable on the many groups of interests the Foundation faces. Is particularly interested in Dr. Wondertainment and Wilson's Wildlife Solutions. Is generally approachable but is often lost in thought, be they mundane or fantastical.

Have a wonderful day!
Dr. Joseph "Joe" Fynegan: Senior researcher at Site-409 and lead on the containment/documentation on several SCPs. Was once suspected of having murdered a fellow Foundation employee but later exonerated of all charges. Expert on ARBH Class Event Scenarios, AKA "Insect Hell" extinction-level events. A little socially awkward and very much an oversized nerd, he has a very relaxed temperament and perhaps a little naïve for someone in his position.

I'm a very boring guy, you know...
Dr. Charles Gears ("COG"): A man strangely lacking in emotional response (to the point of lacking a startle response) and possessing unusual levels of logic and intellect. Former Euclid-class object specialist before having his area of study expanded. Has been deeply involved with research regarding a truly shocking number of SCP objects both major and minor. A figure of great influence in recent Foundation history.

It is not acceptable to inquire that.
Dr. Simon Glass: Head of Psychology. Trusted with performing psychological evaluations of highly ranked Foundation personnel. Very empathetic. Sometimes considered "soft" — and that's true, for a Foundation researcher, but he's still well-trusted. In the course of his interviews, he has gained knowledge of more and more terrible secrets, yet still holds on to both his sanity and empathy.

I talk to everyone, I know everyone...
Dr. Frederick Heiden: Neurology specialist. Anxious, uncertain, empathic, focused on logic. Involved in a number of highly classified projects, despite initially being barred from any non-Safe-classed objects.

Shhhhhh.
Doctor Hoygull: Sapient seagull. Head of the Foundation's Avian Division, commanding MTF-Eta-4, "Begone Thoth".

Dr. Everett King: One of the Foundation's most experienced mathematicians, Doctor King's reputation has nevertheless been overtaken by his testing record involving unusual results. Despite this, he regularly contributes to internal Foundation intellectual periodicals.

I don't want any more goddamn apples.
Dr. Mark Kiryu: Senior researcher and director of an anomalous items processing lab. Upon initial recruitment, had a successful career as a therapist (licensed psychologist). Worked extensively with SCP-1457 in his first years with the Foundation but doesn't talk about that, and has spearheaded several projects involving sapient SCP entities. Cheery attitude and a good listener; looks out for his coworkers and interns like a bit of a mother hen sometimes. Has a ceramic seahorse and potted bamboo on his desk.

Dr. Zyn Kiryu: Highly prolific researcher. Involved in a number of classified Foundation projects. Obsessive, driven, often not eating or sleeping in favor of finishing tasks. Finished her schooling through an accelerated program after joining the Foundation. Initially closed-off and withdrawn, but opened up due to a latent ambitious streak. She often volunteers to handle new Foundation member intake, hoping to give new members a positive introduction to an often deeply horrifying organization. Has a private flair for poetry. Has accidentally inherited the absent Dr. Kondraki's affiliation with anomalous butterflies, including SCP-408 after Kondraki's disappearance.

I didn't ask for this.
Dr. Adam Leeward: Emotionally confused and ethically conflicted humanoid containment specialist from Site-11, living in Site-81. May or may not have made a few mistakes, may or may not have cleaned up a few mistakes. Not without the standard degree of coldness in personality traits, but with a few (sometimes painful) soft spots.

There's something off about you, Lee.
Dr. Sophia Light: Biologist, surgeon and Site Director with far, far too many secrets. A likeable yet frightening person. Blunt, determined, calculating; good under pressure. Putting effort into remaining friendly and open (and emotionally stable). Bears minor facial scarring, and an old injury in her left hand sometimes impairs its functionality. Somewhat traumatic childhood; caretakers forced her to learn outdoor survival by leaving her stranded in the African wilderness for days on end. Joined the Foundation after a classified anomalous incident that killed eleven people, including her then-fiancee. Currently or formerly romantically linked with Troy Lament.

It's not my fault they want another meeting.
Dr. Lillian S. Lillihammer: Genius-level intellect. Master memeticist of Site-43: discoverer, interpreter, neutralizer and creator. Always half a dozen steps ahead of everyone else. Lead researcher on Vikander-Kneed Technical Media. Antisocial and arrogant, but so incredibly competent that nobody begrudges it.

I couldn't explain it to you if I wanted.
Dr. Judith Low: Senior Advisor at the Department of History. Specialises in the religious practices known as Sarkicism, and involved in the containment of SCP-2133, SCP-2191 and SCP-2480.

Dr. Connor MacWarren: Active researcher focusing on the development of anomalous technologies on top of being one of the board of directors at Site-98 in Philadelphia. Currently oversees his own department specializing in extradimensional anomalies. Humble, sarcastic, irritable, and absolutely loathes having to repeat himself every time anyone mishears his dry jokes. Former member of the Marine Corps. with a highly-prolific GOC agent for a father, now estranged.

Hear me out: We make this huge sword...
Dr. Everett Mann: Unconventional medical researcher with few scruples and a specialty in unusual forms of surgery. Jokingly referred to as a "mad scientist". (He objects to the term "mad scientist", claiming that "mad doctor" would be more accurate, and further that the difference should be plain to anyone with a proper academic background to speak of.) Willing to do monstrous things in the name of research. Possesses a dramatic moustache. Due to his upbringing, his cultural and popular knowledges are woefully out of date, leading to anachronistic and ridiculous situations.

Yes, I wanted to show you what I've been working on.
Dr. Jaime Marlowe: Average researcher, specializing in space-time, extra-dimensional, visual, spatial, and cognitohazardous anomalies. Previously described as "painfully, painfully, painfully average", notable more for minor interpersonal incidents and inappropriate outbursts when under stress. Marlowe's profile has slightly increased due to apparent unexplained connections to unrelated anomalous events which only appear to have increased in frequency.

Dr. Placeholder McDoctorate: Head of the 'Pataphysics Department. Initially hired by the I.T. department, promoted to Department Head in 1996 for notable performance in the containment of SCP-5241. Promoted to Site Director, then personally requested reassignment to the 'Pataphysics Department. Promoted to Department Head for notable developments in Theoretical 'Pataphysics, then founded the Archetypicals Division. At some point, had his name retroactively abstracted by SCP-INTEGER.

Dr. Riven Mercer: Veterinary-focused researcher, second-in-command of Kiryu Labs. Handles personnel allocation for incoming anomalous item caches, often goes on outside assignments. Good with animals, owns a grumpy bearded dragon lizard who lives in the lab.

Dr. Ilse Reynders: Non-victim of a disaster which trapped her in what should have been stasis, which she instead turned into an eight-decade self-improvement course. Now possesses sixteen doctorates, the sharpest mind at Site-43 and an unaging brain and body. An early and modern pioneer of Acroamatic Abatement, and potentially future Director of the Temporal Anomalies Department, she was also part of the team which developed the Foundation's Frontispiece glamour to disguise its various front companies.

What time is it?
Dr. Jessie Rivera: Member of Site-120's Director Council. With a Ph.D. in psychology, personally takes care of humanoid anomalies contained at her facility. Close friend of Dr. Daniel Asheworth, working with him on the Damien Nowak case, offering a perspective more grounded in reality. Granddaughter of Hannah Rivera, the person responsible for Site-120's establishment. Married to Magdaleine Cornwell, another member of the Site's Director's Council, with whom she is now peacefully living in the Free Port of Esterberg.

Mag?
Dr. Katherine Sinclair: Acting head - and one of only two members - of the Occult Studies and Thaumatology division at Site-87 in Sloth's Pit, Wisconsin. Has been involved in numerous incidents, including the assault on Sloth's Pit by the now defunct Group of Interest Satyr's Reign, and the 2014 Christmas Incident. Has burn scars on her forearms from a botched flame ritual.

It's not thaumaturgy, it's magic!
Dr. Johannes Sorts: Memetic specialist and field researcher, with a doctorate in art history. Caucasian, late 30s, unshaven with greying brown hair. Slightly overweight, usually wears a grey cap. Obsessive, cowardly and paranoid in mundane situations, but solid and focused when presented with memetic or information based hazards. Multiple disciplinary reports due to poor choice of action under pressure, including the shooting of a guard while under my influence. Currently under psychiatric evaluation and restricted to safer projects.

The fucking Foundation and that fucking toaster.
Dr. Cole Thereven: Director of the Department of Anomalous Communications and Relations, researcher at Site-63. Involved in some ethically questionable research projects. Far more important to the Foundation than he initially seems.

Dr. William W. Wettle: Head of Replication Studies at Site-43. Nobody's favourite person. Untalented, unintelligent, unmotivated, unpleasant, unfortunate. Staunchly resists character development, career advancement and friendship formation. Somehow nevertheless vital to the continued survival of the prime timeline. Frequent interrogator of Vikander-Kneed Technical Media anomalies, almost always against his will. May have hidden depths.

What do I put here
Dr. Thaddeus Xyank: Presently low-level but extremely significant Foundation researcher. Specializes in temporal anomalies. Somewhat arrogant and long-winded, but considered an up-and-coming genius.

Where is he? Where isn't he?""", "green"))
  if scpinput == "dc":
    print(colored("""D-952 (formerly Veronica Fitzroy): Anartist musician, co-founder of the "House of Spades" rock band, partially responsible for the creation of SCP-952. In custody following two failed suicide attempts, designated D-952. Missing, presumed deceased.

D-7294: Former professional cellist with a history of violent behavior towards women. Useful enough to be exempt from monthly termination, but should be kept away from female personnel.

D-11424 (formerly Tony Marquez): Notable for surviving many experiments, some involving dangerous anomalies, and so considered an exploration specialist. Now deceased, number reassigned.

""", "green"))
  if scpinput == "rc":
    print(colored("""Professor Anders Bjornsen: Field researcher specializing in anomalous psychologies and societal abnormalities, working as an SCP Analyst for the Psychology Department. Previously assigned to the Memetics Department, Theology & Theometrics Department, and Cognitohazard Research Department. Respected for remaining calm during multiple containment breaches.

Researcher Jacob Conwell: Anomalous Materials Analyst. Masters Degree in Analytical Chemistry. Current head of the Site-64 AMat Lab. Frequently called upon, Conwell has made a name for himself in the Foundation as a hard worker.

I'm doing so much these days.
Researcher Rose Labelle: Researcher of Anomalous Programs & Computer Software in the Foundation I.T. Department. Involved in the containment of SCP-3860 (see files on the Anderson Robotics Group of Interest). Otherwise unremarkable, all rumors of anomalous expertise and feats are completely untrue.

Will be present when it ends.

Researcher Samuel M. Lloyd: English memeticist and part-time Hazardous Materials Containment Liaison Supervisor who shows up all over the place. Likes to keep tabs on whatever's going on, and likes interacting with anomalies more than is good for him. Cynical, self-centred and in over his head, but generally well-meaning. Younger than you'd expect.

Just remember...
Technical Researcher David Rosen: Technical Advisor and Researcher. Responsible for ensuring the continued functionality of Site-19's technical infrastructure. Known for being acerbic and marginally accident-prone, he also manages the facilities technical department very well and is widely see as a thrifty leader.

You want me to what?
Junior Researcher James: Wrote Special Containment Procedures for SCP-078, SCP-682, SCP-789, SCP-8231 and SCP-9000 before going AWOL to found the kA0s insuRgnc3e

Seriously, who uploaded this into the database? Need a witness for summary deletion.""", "green"))
  if scpinput == "di":
    print(colored("""Director Jean Karlyle Aktus: Director of Site-81. A seemingly impossibly old man, known for his analytic approach to containment leading to thorough and successful containment procedures. Aktus serves as the head of the Foundation's Classification Committee, and is also involved with several exotic mobile task forces, including Alpha-9 and Kappa-10.

Won't you spare me over ‘til a another year?
Dr. Charles Anborough: Director of Sites 59 and 117, Keter containment specialist. Curious and crippled, a nuclear physicist who can't seem to stay away from cataclysmic threats. Fortunately, through an absurd combination of improvisation and miracles, he seems to be the best man for the job. His sad smile and dry humor belie the confused past of a man always searching for answers.

I fucking hate you!
Director Calvin Bold: Director and founder of the Decommissioning Department, former researcher and Ethics Committee liaison. A somewhat controversial figure, particularly for the department which he runs. Somewhat alien-looking, possessing a skeletal hand and crystals for eyes after an accident with SCP-212. Despite being generally mild-mannered and amiable, works to keep any possible variables under control, and trusts himself more than anyone else, often to a fault.

I know myself better than anyone.
Director Julian Corwin: A veteran of the Seventh Occult War, Julian Corwin served as a Foundation field agent for four decades before finally accepting an administrative position as Site Director of Site-246, where he was responsible for overseeing the operations of Mobile Task Force Delta-3 ("Solomon's Hand"). His extensive field experience, general disinterest in administrative politics, and reputation for level-headed leadership made him a clear choice to manage the pilot project of the Special Asset Task Force Program. Following the dissolution of Delta-3 in 1990, he received a lateral promotion to Site-64, where he served as Site Director until 1998.

His service record since 1998 is classified.

Director Ruslav Diaghilev: Director Diaghilev has been involved with the Foundation for an unknown period of time, but currently heads the Alchemy Department from Site-127. Director Diaghilev is the resident expert on Alchemical phenomena and has assisted in the containment of several alchemic SCP objects. Additionally, any and all alchemic creatures fall under his purview, though outside consultants may be required from time to time.

Director Diaghilev is the primary contact and educator for Foundation Alchemists on staff. Any and all requests for consultation can be directed to his office. Additionally, Director Diaghilev is assigned a personal MTF for the recovery of significant alchemic objects.

Alchemy is all around us, and flows through us, constantly striving for balance.
Director Shirley Gillespie and Dr. Ralph Roget: Director Shirley Gillespie is a part of the oldest guard in the Foundation — holding a directorship in Site-77, a storage facility now disguised as an Amazon.com shipping center, for over fifty years. Although constantly rumored to be retiring, she still exerts influence, sometimes through her grandson, Dr. Ralph Roget.

Don't worry, you're going to blow them all away.
Director Maria Jones: Director of Records and Information Security Administration (RAISA). Powerful and isolated, Director Jones controls much of the ebb and flow of information across the Foundation, both inside and between facilities. She has few friends, but is loyal to those few she has. Everyone knows her name as a matter of course, but few people know her.

Sheldon Katz, esq: The Foundation's Senior Legal Consultant, head of the Foundation's Legal Department, which handles legal matters both mundane and anomalous. Katz's legal acumen has earned the respect of everything from demonic entities to higher powers.

Director Paul Lague: Director of Site-322 and head of the Integration program, a project aimed at employing the useful abilities of anomalies in containment. Tries to be diplomatic and work closely with other sites that take a similar approach, although on occasion he is disappointed that other Foundation personnel do not share this attitude.

Director Allan James McInnis: Director of Site-43. Born in England, educated at Eton College and trained at Site-91 before moving to Canada. Calm under pressure. Gets the best out of his staff without excessive discipline due to his background in communications.

Director Kate McTiriss: Straight-laced director of Foundation operations in Region 352, the Gulf Coast of the United States of America.

Dr. Tilda D. Moose: Current Site Director of Site-19 and Co-Director of Site-17, having inherited the positions from a string of previous Directors. Stern, anxious, mildly obsessive. Can become overly passionate once something gets her going. Considered to have an outsized degree of influence given relatively short official length of tenure with the Foundation (under a decade). Some of Site-19's bureaucracy sees her as a figurehead, whether accurately or not.

You don't need to worry about me. I'm not biting off more than I can chew this time.
Director Simon Pietrykau: Former GRU Division "P" researcher "Iceman", defected to the Foundation after the Cuban Missile Crisis. Quickly rose through the ranks to found the Department of Analytics, and is now its Director. Considered an expert on "eigenweapons".

Director Cody Westbrook: The former protege of Julian Corwin, Cody Westbrook was directly recruited through the Foundation Service Academy, graduating fourth in his class at Cheyenne Point. After service with MTF Omega-17 ("Florida Men") and MTF Sigma-23 ("Wily Coyotes"), he was assigned as the handler for Special Asset Agent Firestarter and given command of MTF Delta-3 ("Solomon's Hand"), becoming one of the youngest MTF commanders at the time. He compiled an exemplary service record with Delta-3, until its dissolution following the loss of Agent Firestarter. An internal inquiry board chaired by Analytics Director Simon Pietrykau assigned no fault to Agent Westbrook, but the incident marred his reputation.

After Delta-3 was dissolved, Westbrook was promoted to Site Director of Site-246 to fill the vacancy left by Director Corwin's transfer to Site-64. He has served in that role ever since.

Marion Wheeler: Claims to be the Chief of the Antimemetics Division, despite the fact that there is no Antimemetics Division. She somehow still has full Foundation credentials, a security breach that is currently under investigation.""", "green"))
  if scpinput == "sc":
    print(colored("""SCP-035 AKA "The Possessive Mask": A white porcelain mask constantly secreting a corrosive black substance. Capable of taking possession of anyone wearing it, displaying an intelligent but sadistic personality, skilled at manipulation. Also capable of exerting anomalous effects on its surroundings if not regularly provided with new hosts. Has taken an interest in SCP-682 as an indestructible host.

It is suspected that SCP-035 was once a resident of Alagadda, the Court of the Hanged King, specifically as the Black Lord, Wearer of the Anguished Mask.

SCP-049 AKA "The Plague Doctor": A humanoid entity resembling a medieval plague doctor. He is obsessed with curing an alleged illness known only as "The Pestilence", often by killing "infected" patients with a single touch of his hand, and then performing anomalous surgery to convert the victims into mindless undead creatures designated SCP-049-2.

SCP-073 AKA "Cain": An ancient, immortal male humanoid. Amiable and calm, generally helpful towards Foundation staff, though prefers to keep some aspects of his past hidden.

I am glad to help you.
SCP-076-2 AKA "Able": An ancient, immortal male humanoid. Incredibly violent and with little respect for human life, he somehow came to an agreement with the Foundation and became a member of their first anomalous task force, MTF Omega-7 ("Pandora's Box"). While his thirst for blood was initially kept under control, he eventually grew weary of Foundation control and snapped, killing most of his comrades. Currently kept in maximum-security containment.

War is my nature.
SCP-079 AKA Old AI: SCP-079 is an Exidy Sorcerer microcomputer containing an advanced artificial intelligence. It was built in 1978 as a continuously evolving and self-improving intelligence, and has advanced well beyond the capabilities of its hardware. Certain anomalous elements of its code have been reverse engineered for the creation of [REDACTED]. It is capable of holding a conversation, but due to limited memory it can only recall events in the last 35 hours. There are notable exceptions, such as consistently recalling an encounter with SCP-682, and never forgetting its desire to escape containment and upload itself onto more powerful hardware.

SCP-096 AKA "The Shy Guy": A pale, emaciated humanoid that violently attacks anyone who observes its face, regardless of distance. It is capable of moving at incredible speed towards any observer, undeterred by barriers and impervious to conventional weaponry. Due to the danger that images of its face may exist outside of Foundation custody, termination has been approved and is pending on a viable proposal from Dr. Dan ███████. Origin is unknown.

Proposals for the neutralisation of SCP-096 have included placing SCP-035 on its face, having SCP-173 break its neck then terminating it while vulnerable, sending it into an another reality, and launching it into the sun as soon as a way to do so is available.

SCP-105 AKA Iris Thompson: A female human with the anomalous ability to manipulate objects depicted in photographs. Recruited into Mobile Task Force Omega-7 ("Pandora's Box") and given low-level security clearance, but returned to containment in Site-17 after MTF Omega-7 was disbanded.

Seems like the story's over...
SCP-106 AKA "The Old Man": Humanoid entity of varying appearance, but always elderly and rotting. Has a corrosive effect on solid materials, and the ability to enter and exit from its own pocket dimension. Characterised by a disturbing intelligence while hunting its victims. Despite extensive historical research, its origin is completely unknown.

SCP-173 AKA "The Sculpture": Animate statue constructed from concrete, rebar and spray paint. Moved to Site-19 in 1993. Cannot move while observed, attacks with bone breaking force if anyone blinks. Produces a mixture of blood and faeces, floor must be cleaned on a bi-weekly basis.

Creator and origin completely unknown, presumed to be some sort of art project. Rumored to date back to the beginning of the Foundation. May not be the only one of its kind, although appearances vary greatly.

SCP-179 AKA Sauelsuesor: Humanoid female figure located in a fixed position below Earth's sun. Her skin and 34 km long hair are made of an unidentified matte black material, with golden astrological symbols on various locations on her body. Through unknown means, SCP-179 can detect and point to extraterrestrial threats to Earth, both anomalous and non-anomalous. Communication via probe has revealed that this entity speaks fluent French, and claims to be "the lookout" and the "sister of the sun", although she also claims to have come from Earth at an unknown point in the past.

SCP-239 AKA Sigurrós "Siggy" Stefánsdóttir: 8-year-old human girl and immensely powerful reality bender, commonly known as the "Witch Child". Formerly contained by an elaborate ruse wherein Foundation personnel convinced her she was a witch-in-training; this didn't quite work. After an unauthorized termination was attempted by Dr. Clef (possibly while under her unconscious influence), she has been kept in a medically-induced coma, although keeping her from waking does not completely neutralise her power. May possess godlike abilities; may in fact be God, or at least a friend and possible protégé. Or perhaps she's just a little girl with too much power.

SCP-343 AKA "God": An elderly human male with apparent omnipotence, willingly held within Site-17 and permitted to interact with staff and other SCP objects.

No way he's who he says he is...
SCP-423 AKA "Fred": A metafictional entity who only exists in text and documents, notable for his ability to appear in any written narrative he chooses, although always as a minor character.

SCP-507 AKA "Grabnok the Destroyer": A male human with the involuntary ability to regularly shift into alternative realities, widely known as "The Dimension Hopper". Answers to many names, but his most ridiculous suggestion seems to have stuck. Since full containment is impossible, SCP-507 is given an unusual amount of freedom, and has even been allowed to interact with other anomalies in containment. Multiple versions exist, and can even encounter one another if present in the same reality at the same time. At least one version is a member of the Serpent's Hand Group of Interest.

SCP-527 AKA "Mr. Fish": A humanoid entity, one of Dr. Wondertainment's Little Misters, whose only anomalous quality is that he bears the head of a fish.

SCP-682 AKA "The Hard-to-Destroy Reptile": A seemingly indestructible and highly adaptive reptilian creature that the Foundation has been unable to terminate, despite many attempts using both mundane and anomalous means. Driven by an intense omnicidal rage and hatred for all life, its containment breaches have cost the Foundation an incalculable amount of resources and personnel.

You are... 
SCP-993 AKA "Bobble the Clown": A living animated character from an anomalous television series of the same name. Teaches children under 10 about murder and torture while adults are asleep. Despite the initial success of Protocol Upsilon-Beta 3, multiple containment breaches have been reported.

SCP-1233 AKA "Moon Champion": An anomalous humanoid entity that appears to be wearing a spacesuit. This self-proclaimed "Champion of the Moon" is apparently recruiting people to fight the "Moon Monsters" plaguing the "Moon Kingdom". May be of use to the Foundation, under the right circumstances.

SCP-1867 AKA Lord Theodore Thomas Blackwood: Gentleman explorer turned sea slug, known for Munchausean tales of adventure and derring-do in exotic lands.

I dare say, there must be more to it than that!
SCP-2085 AKA The Black Rabbit Company: A sextet of anarchist cyborg troublemakers. Boss, Momoko, Hana, Nanami, Tomi, and Wizard (AKA Space Wizard and the Commando Catgirls) are out to stick it to the man and get into space while doing so. Armed with guts, hot bloodedness, and many, many bullets.

An adaptation by Bones Studio of their rumoured spaceship theft has been confirmed for the winter 2018 season never.

SCP-2273 AKA Major Alexei Belitrov: This male humanoid is contained at Site-17 in most observed realities. Aliases include "Father Anvil" and "Roach". Classified as a Type-B Sapient Anomaly, Alexei Belitrov has been compliant and cooperative with the Foundation in Baseline reality and most observed derivatives. He is fluent in Russian and German and has excelled in his English lessons. Alexei is believed to be of extra-universal origin, and claims to have a military background despite a general aversion to violence. However, if his claims of combat experience and memory retention are to be believed, it is likely that Alexei Belitrov remains capable of acts of armed violence.

Additionally, in Reality Construct FZ27GO, multiple persons resembling Alexei Belitrov spontaneously manifested, and were frequently sighted fighting at nighttime. In most occasions, these iterations of Alexei Belitrov are accompanied by a unidentified human with a red tattoo on one of their hands.

●●|●●●●●|●●|● / ●●●●●●●●●●:

SCP-2337 AKA "Dr. Spanko": A sapient male corncrake bird, capable of speaking extremely loudly in a strange quasi-English vernacular that is very difficult to decipher.

It me! Cack! Cack! Cack!

SCP-2721 AKA "Lyris" and "Eli"/"bones": The two halves of an alien satellite with significant online presence. SCP-2721-LYRE ("Lyris") identifies as a transwoman and blogs about social justice issues and the webcomic Homestuck. SCP-2721-LORD ("Eli") runs a personal blog and is believed to act as a moderator for the "Gamers Against Weed" chat, under the username "bones".

SCP-2852 AKA "Cousin Johnny": A humanoid entity composed of muscle and chitin. It makes appearances at baptisms, weddings and funerals, causing long-term psychological damage to everyone involved. Under observation, but cannot be fully contained. Association with cicadas suggests a connection with SCP-3004, SCP-5349 and SCP-5852.

SCP-3090 AKA Heather Mason: A humanoid entity with a CRT television set for a head, and the anomalous ability to interface with and influence electronic devices. Co-created by two members of "Gamers Against Weed" as a parody of Dr. Wondertainment's Little Misters, and given the title "Ms. Mad About Video Games".

Breached containment. Now believed to inhabit The Void.

SCP-3774-2432 AKA "Leslie": A sapient female mosquito, notable for having four children with a male human. Returned to life by SCP-049.

SCP-4051 AKA Rainer Miller: Human male with the anomalous ability to manifest wormholes and retrieve "objects" from them (including phenomena such as fire, and non-existent concepts). Although SCP-4051's abilities have previously been utilised by the Foundation, this individual is currently contained as a Keter-class object with a high risk of breaching containment.

{INPUT 4/4051 CLEARANCE}
SCP-4494 AKA The Specter: Fighter of criminals and bringer of justice — The Specter is the physical embodiment of fighting crime! Capable of moving through shadows and manifesting weapons at will, The Specter's powerful resolve to defend even the laws of physics has proven useful to The Foundation, and he has been recruited into Mobile Task Force Alpha-9 ("Last Hope"), working alongside other anomalous operatives.

SCP-4768 AKA Ulysses B. Donkman: A male humanoid bearing the head of a donkey. Despite his unusual appearance, he is capable of altering perception of himself and his surroundings, both for thematic and for stealth purposes. Of substantial age, known to have been active since the early 19th century. Lauded for his strength, skill and chivalry. Participant in many bold adventures and daring escapes often considered to be more legend than fact.

I hear some of y'all like to call me half-assed.
SCP-5056-B AKA Philip Eugene Deering: Constantly verbally abused by the other half of the SCP-5056 anomaly, a mirror monster that Deering affectionately refers to as "Doug". While this entity usually disregards others, it will become dangerously aggresive if Deering is threatened. Deering is otherwise unremarkable, a career janitor at Site-43 with no ambition, no ego, and no hope of promotion. Gentle and good-natured, but capable of acts of bravery when necessary. In an extremely stable romantic relationship with Security Chief Torosyan.

SCP-6599 AKA HOGSLICE consists of a series of online accounts that are consistently hostile, argumentative and boastful. Upon provocation by a member of an online community, SCP-6599-1, a humanoid entity resembling professional wrestler Scott Rechsteiner, physically manifests to verbally abuse and physically assault its chosen target. While attacks upon non-anomalous humans typically end in hospitalisation, interactions with other anomalous entities have had less predictable results.

WHAT EVEN IS THIS""", "green"))
  elif scpinput.isnumeric:
    try:
      print(colored(scpscraper.get_scp(scpinput), "green"))
    except:
      pass
    try:
      print(colored(scpscraper.get_scp(scpinput)["content"]["Object Class"], "green"))
    except:
      pass
    try:
      print(colored(scpscraper.get_scp(scpinput)["content"]["Special Containment Procedures"], "green"))
    except:
      pass
    try:
      print(scpscraper.get_scp(scpinput)["image"]["src"])
    except:
      pass