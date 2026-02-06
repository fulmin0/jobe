# Product Sense Mock Interview for DOORDASH

- **Source:** https://www.youtube.com/watch?v=dz-hqOih9qY
- **Channel:** Dianna Yau
- **Duration:** 33:15
- **Question Types:** product-sense
- **Frameworks Covered:** marketplace metrics selection, user journey mapping, pain point severity assessment, preventative vs. reactive solutions
- **Difficulty Level:** intermediate

## Summary
This mock interview features Yoon, a new PM at DoorDash (previously Microsoft), tackling an Airbnb question: "How would you fix the worst post-booking experience?" The interview demonstrates strong structure, user empathy through personal anecdotes, and thoughtful metrics selection. Yoon navigates the challenge of retention metrics for infrequent-use products, maps an exhaustive list of pain points for both guests and hosts, and develops a two-pronged solution approach: preventative measures and reactive recovery.

## Key Takeaways
1. Retention metrics are difficult for infrequent-use products (travel) - people not returning may be due to travel frequency, not bad experience
2. Number of nights booked successfully captures value for all parties in a marketplace (hosts, guests, platform)
3. Marketplace products require considering pain points for both supply (hosts) and demand (guests) sides
4. Personal experiences provide powerful user empathy - use them to bring pain points to life
5. Preventative solutions reduce problem occurrence; reactive solutions handle inevitable edge cases well
6. Severity of pain matters more than frequency for "worst experience" questions
7. Clear decision criteria at every step (metrics, users, pain points, solutions) demonstrates structured thinking

## Frameworks & Techniques Demonstrated

### Airbnb Business Understanding
- **Product:** Marketplace for owners to rent places, guests to stay (vs. hotels - more homey, local)
- **Users:** Hosts (owners renting places), Guests (people booking places)
- **Business Model:** Transaction fees on every booking/night stayed

### Metrics Brainstorming & Selection

#### Considered Metrics
1. **Number of nights booked and stayed per day** [SELECTED]
   - Intersection of all three parties' value
   - Hosts: Make money when nights booked
   - Guests: Get value when they successfully stay
   - Airbnb: Revenue from each transaction
   - Reflects successful completion, not just booking

2. Retention
   - REJECTED: Hard to measure for infrequent travel
   - Can't distinguish bad experience from low travel frequency
   - May travel to places without Airbnb options

3. Rating
   - REJECTED: Not representative - only extreme experiences get rated
   - Most users don't leave ratings

### Post-Booking Pain Points Map

#### Guest Pain Points (8 identified)
1. **Cancellation charges high fee** - Painful when budget-constrained
2. Hard to find the place - Maui forest example, no information on listing
3. **Can't check in / No room available** - Highest pain (no place to stay) [PRIORITIZED]
   - Multiple causes: Room not actually available, confirmation issues
   - Personal story: Host hadn't done Airbnb in a while, room unavailable
4. **No key or password works** - Medium pain (eventually solvable via host/support)
5. **Place not clean** - Annoying but not highest pain, depends on severity
6. Place doesn't match photos - Pictures always nicer
7. Supplies/equipment not working - Refrigerator, toilet issues
8. Safety concerns
   - Neighborhood feels unsafe (new place, first time)
   - Sharing with strangers (don't know roommates, insecure locks)
   - Extreme: Dangerous accidents (fire, gas leak)
9. Host not responding - Frustrating when need help
10. Bad customer service - Issues not resolved by support

#### Host Pain Points (2 identified)
1. Guests damage house - Small to large damage
   - Medium pain level (varies by severity)
   - Low frequency
   - Doesn't prevent continued hosting

2. Late checkout - Messes up next guest check-in, cleaning schedule
   - Low to medium pain
   - Low to medium frequency
   - Doesn't stop hosting (blame the guest)

### Prioritization Criteria
- **Pain level** - How painful is this experience?
- **Impact on metrics** - Effect on "nights booked and stayed"
- **Frequency** - How often does this happen?
  - Note: Weighted less for "worst experience" question
  - 1% of large user base is still significant

### Top Pain Point Analysis: No Room Available
- **Pain level:** HIGH - Worst of all pain points (literally no place to stay)
- **Impact on metrics:** HIGH
  - Direct impact: One night NOT booked/stayed
  - Future impact: Won't trust Airbnb, won't return
- **Frequency:** LOW - But 1% of Airbnb's huge user base is still many people
- **Rationale:** Even low frequency justified for worst experience with highest pain and impact

## Sample Questions Covered
- "How would you fix Airbnb's worst post-booking experience?"
- Implicit: What metrics matter? Which users? What problems exist? How do we prioritize?

## Common Mistakes Highlighted
- Choosing retention for infrequent-use products without acknowledging measurement challenges
- Not considering both sides of marketplace (only guests, forgetting hosts)
- Listing pain points without clear prioritization criteria
- Not using personal experiences to demonstrate user empathy
- Weighing frequency equally for "worst experience" questions (should weight pain/impact more)

## Notable Quotes / Tips
- "I find retention really hard to measure here - if they don't come back in a year, you can't say it's because of bad experience. They might just not travel that frequently"
- "Number of nights booked is intersection of all three parties - host gets value, guest gets value, Airbnb gets value"
- "When I think about the worst post-booking experience, I think about things that can go wrong"
- "No room available - that's the highest pain point here. You don't have a place to stay. Others, you have a place, it's just something not working"
- "I would weight frequency less for 'worst experience' - even 1% of Airbnb users is still a large user group"
- "I bucket solutions into two: How to prevent it happening, and when it really happens, what we do? You can't make everything perfect, but if you make up for it, users can still be happy"

## Solutions Proposed

### Bucket 1: Prevention (Stop Problem Before It Happens)

#### Solution 1a: Inactive Host Detection
- Use machine learning to identify inactive hosts
- Signals: No customer conversations in X months, no listing edits, no activity
- Automatically remove listings for inactive hosts
- Prevents bookings for unavailable properties

#### Solution 1b: Confirmation Check with Guest
- Guest books → system checks host responsiveness
- If host hasn't responded for a while, send reminder/confirmation to guest
- Example: "Your booking hasn't been confirmed. Host hasn't responded. Double-check before traveling"
- Catches issues before guest arrives

### Bucket 2: Recovery (Handle When It Happens Anyway)

#### Solution 2a: Priority Airbnb Booking
- Guest arrives, no room available → immediate priority access
- Find nearby Airbnb alternatives
- Guarantee booking even at higher price
- Airbnb covers cost difference

#### Solution 2b: Hotel Partnerships
- In locations with limited Airbnb inventory
- Partnership with hotel chains for backup options
- Offer free hotel stay when Airbnb falls through
- Ensures guest has guaranteed place

#### Solution 2c: RV/Camping Van Alternative (Creative)
- Target adventurous Airbnb users
- Offer unique RV or camping van experience
- Turn negative (no room) into positive (fun unique experience)
- Changes mindset: "Airbnb is fun and interesting"
- Similar to Airbnb Icons (owned unique properties)

### Solution Philosophy
"You can't make everything perfect, but if you can make up for it, users can still be happy and choose Airbnb. Their customer service is so good."

## Interview Strengths (Debrief Notes)
1. **Clear structure** - Walked through framework upfront, organized each section
2. **User empathy** - Personal Maui story, understanding frustrations
3. **Decision criteria** - Explicit criteria for metrics, pain points, solutions
4. **Preventative vs. reactive** - Two-pronged approach shows comprehensive thinking

## Additional Context
- Video provides rare DoorDash interview content (limited information available online)
- Yoon recently joined DoorDash, providing current insights
- Question framed around Airbnb but demonstrates approach for any marketplace product
- Structure applicable to DoorDash's marketplace dynamics (restaurants, dashers, customers)
