# realtime-trains-api-micropython README

This was originally meant to be a fork of <https://github.com/DoddyUK/rtt-api-python> for MicroPython,
however due to the large responses (often up to 40KB) these are just too large to safely handle
on microprocessors. RTT has no way to limit the number of services returned so as such this will be
archived. I may come back to this in the future, but for now anyone stumbling across this my
recommendation is to use an intermediary device (eg a Rasp Pi 4 or server, basically anything without
memory limitations) to both limit the number of services and remove unnecessary attributes.

For reference I have done some limited debugging and even a small station which returns a 1KB
response is not easily dealt with, even with aggressive use of manual garbage collection.
