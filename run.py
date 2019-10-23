import logging
import time

log = logging.getLogger(__name__)
log.addHandler(logging.StreamHandler())
log.setLevel(logging.INFO)


def main():
    start = time.time()

    end = time.time()

    log.info('Done')
    log.info('The process took %s seconds to run' % (end - start))


if __name__ == '__main__':
    main()
